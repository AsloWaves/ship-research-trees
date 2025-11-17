using System;
using System.Collections.Generic;
using UnityEngine;
using Mirror;
using WOS.Networking.Managers;

namespace WOS.Chat
{
    /// <summary>
    /// Server-authoritative chat manager using Mirror networking
    /// Handles message routing, validation, spam throttling, and profanity filtering
    /// Phase 1: System, World, and Proximity text chat
    /// </summary>
    public class ChatManager : NetworkBehaviour
    {
        [Header("Spam Protection")]
        [Tooltip("Maximum messages per time window")]
        public int maxMessagesPerWindow = 3;

        [Tooltip("Time window for spam detection (seconds)")]
        public float spamWindowSeconds = 5f;

        [Header("Profanity Filter")]
        [Tooltip("Enable basic profanity filter")]
        public bool enableProfanityFilter = true;

        [Tooltip("Replacement string for filtered words")]
        public string filterReplacement = "***";

        [Header("Proximity Chat")]
        [Tooltip("Maximum distance for proximity chat (in Unity units)")]
        public float proximityRange = 50f;

        // Server-only: Track message timestamps per connection for spam detection
        private Dictionary<NetworkConnectionToClient, Queue<float>> messageTimestamps = new Dictionary<NetworkConnectionToClient, Queue<float>>();

        // Server-only: Map connections to player names
        private Dictionary<NetworkConnectionToClient, string> playerNames = new Dictionary<NetworkConnectionToClient, string>();

        // Basic profanity word list (server-side only)
        private HashSet<string> profanityList = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
        {
            // Add common profane words here - keeping minimal for now
            "damn", "hell", "crap", "shit", "fuck", "ass", "bitch"
        };

        #region Server

        public override void OnStartServer()
        {
            messageTimestamps.Clear();
            playerNames.Clear();
            Debug.Log("[ChatManager] Server started - ready to process messages");
        }

        public override void OnStopServer()
        {
            messageTimestamps.Clear();
            playerNames.Clear();
        }

        /// <summary>
        /// Client sends chat message to server
        /// Server validates, processes, and broadcasts to appropriate recipients
        /// </summary>
        [Command(requiresAuthority = false)]
        public void CmdSendMessage(string content, ChatChannel channel, NetworkConnectionToClient sender = null)
        {
            // Validate sender
            if (sender == null || sender.identity == null)
            {
                Debug.LogWarning("[ChatManager] Invalid sender - rejected");
                return;
            }

            // Get or register player name
            if (!playerNames.ContainsKey(sender))
            {
                string playerName = GetPlayerName(sender);
                playerNames[sender] = playerName;
                Debug.Log($"[ChatManager] Registered player: {playerName}");
            }

            string senderName = playerNames[sender];

            // Spam check
            if (IsSpamming(sender))
            {
                TargetSpamWarning(sender, "You're sending messages too quickly!");
                Debug.LogWarning($"[ChatManager] {senderName} is spamming - message rejected");
                return;
            }

            // Validate content
            if (string.IsNullOrWhiteSpace(content))
            {
                Debug.LogWarning($"[ChatManager] {senderName} sent empty message - rejected");
                return;
            }

            // Apply profanity filter
            string filteredContent = enableProfanityFilter ? FilterProfanity(content.Trim()) : content.Trim();

            // Create message
            ChatMessage message = new ChatMessage(senderName, filteredContent, channel);

            // Route message based on channel
            switch (channel)
            {
                case ChatChannel.World:
                    RpcReceiveMessage(message);
                    Debug.Log($"[ChatManager] {senderName} → World: {filteredContent}");
                    break;

                case ChatChannel.Proximity:
                    // Server-side proximity filtering - only send to nearby players
                    SendProximityMessage(sender, message);
                    Debug.Log($"[ChatManager] {senderName} → Proximity: {filteredContent}");
                    break;

                case ChatChannel.System:
                    // System messages should only come from server
                    Debug.LogWarning($"[ChatManager] {senderName} tried to send System message - rejected");
                    return;

                default:
                    Debug.LogWarning($"[ChatManager] {senderName} sent to unimplemented channel: {channel}");
                    TargetChannelUnavailable(sender, channel);
                    return;
            }
        }

        /// <summary>
        /// Server broadcasts system message to all clients
        /// </summary>
        [Server]
        public void SendSystemMessage(string content, MessagePriority priority = MessagePriority.Normal)
        {
            ChatMessage message = new ChatMessage("", content, ChatChannel.System, priority);
            RpcReceiveMessage(message);
            Debug.Log($"[ChatManager] System → All: {content}");
        }

        /// <summary>
        /// Get player name from connection (checks for Player component)
        /// </summary>
        private string GetPlayerName(NetworkConnectionToClient conn)
        {
            // Get username from AuthenticationManager
            if (AuthenticationManager.Instance != null)
            {
                string username = AuthenticationManager.Instance.GetUsername(conn.connectionId);
                if (!string.IsNullOrEmpty(username))
                {
                    return username;
                }
            }

            // Fallback to connection ID if authentication not found
            return $"Player{conn.connectionId}";
        }

        /// <summary>
        /// Check if player is sending messages too quickly
        /// </summary>
        private bool IsSpamming(NetworkConnectionToClient conn)
        {
            if (!messageTimestamps.ContainsKey(conn))
            {
                messageTimestamps[conn] = new Queue<float>();
            }

            var timestamps = messageTimestamps[conn];
            float currentTime = Time.time;

            // Remove old timestamps outside the window
            while (timestamps.Count > 0 && currentTime - timestamps.Peek() > spamWindowSeconds)
            {
                timestamps.Dequeue();
            }

            // Check if too many messages in window
            if (timestamps.Count >= maxMessagesPerWindow)
            {
                return true;
            }

            // Add current timestamp
            timestamps.Enqueue(currentTime);
            return false;
        }

        /// <summary>
        /// Apply profanity filter to message content
        /// </summary>
        private string FilterProfanity(string content)
        {
            string filtered = content;

            foreach (string word in profanityList)
            {
                // Case-insensitive replacement
                filtered = System.Text.RegularExpressions.Regex.Replace(
                    filtered,
                    $@"\b{word}\b",
                    filterReplacement,
                    System.Text.RegularExpressions.RegexOptions.IgnoreCase
                );
            }

            return filtered;
        }

        /// <summary>
        /// Notify specific client they're being rate limited
        /// </summary>
        [TargetRpc]
        private void TargetSpamWarning(NetworkConnection target, string warning)
        {
            ChatMessage message = new ChatMessage("", warning, ChatChannel.System, MessagePriority.Important);

            // Find ChatHistory and add message locally
            ChatHistory history = FindFirstObjectByType<ChatHistory>();
            if (history != null)
            {
                history.AddMessage(message);
            }
        }

        /// <summary>
        /// Notify client that channel is not yet available
        /// </summary>
        [TargetRpc]
        private void TargetChannelUnavailable(NetworkConnection target, ChatChannel channel)
        {
            ChatMessage message = new ChatMessage("", $"The {channel} channel is not yet available.", ChatChannel.System);

            ChatHistory history = FindFirstObjectByType<ChatHistory>();
            if (history != null)
            {
                history.AddMessage(message);
            }
        }

        /// <summary>
        /// Send proximity chat message to all players within range
        /// Server-side spatial filtering for realistic proximity chat
        /// </summary>
        [Server]
        private void SendProximityMessage(NetworkConnectionToClient sender, ChatMessage message)
        {
            if (sender == null || sender.identity == null)
            {
                Debug.LogWarning("[ChatManager] SendProximityMessage: Invalid sender identity");
                return;
            }

            Vector3 senderPosition = sender.identity.transform.position;
            int recipientCount = 0;

            // Iterate through all connected players
            foreach (var conn in NetworkServer.connections.Values)
            {
                if (conn == null || conn.identity == null) continue;

                Vector3 receiverPosition = conn.identity.transform.position;
                float distance = Vector3.Distance(senderPosition, receiverPosition);

                // Send message if within proximity range
                if (distance <= proximityRange)
                {
                    TargetReceiveProximityMessage(conn, message);
                    recipientCount++;
                }
            }

            Debug.Log($"[ChatManager] Proximity message sent to {recipientCount} nearby players (range: {proximityRange} units)");
        }

        /// <summary>
        /// Receive proximity chat message on specific client
        /// Only called for players within proximity range
        /// </summary>
        [TargetRpc]
        private void TargetReceiveProximityMessage(NetworkConnection target, ChatMessage message)
        {
            ChatHistory history = FindFirstObjectByType<ChatHistory>();
            if (history != null)
            {
                history.AddMessage(message);
                Debug.Log($"[ChatManager] Received proximity: [{message.channel}] {message.sender}: {message.content}");
            }
            else
            {
                Debug.LogWarning("[ChatManager] ChatHistory not found - proximity message dropped");
            }
        }

        #endregion

        #region Client

        /// <summary>
        /// Receive chat message from server (all clients)
        /// </summary>
        [ClientRpc]
        private void RpcReceiveMessage(ChatMessage message)
        {
            // Find ChatHistory and add message
            ChatHistory history = FindFirstObjectByType<ChatHistory>();
            if (history != null)
            {
                history.AddMessage(message);
                Debug.Log($"[ChatManager] Received: [{message.channel}] {message.sender}: {message.content}");
            }
            else
            {
                Debug.LogWarning("[ChatManager] ChatHistory not found - message dropped");
            }
        }

        #endregion
    }
}
