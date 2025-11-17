using UnityEngine;
using System.Collections.Generic;
using Unity.Mathematics;
using WOS.Debugging;
using WOS.ScriptableObjects;

namespace WOS.Environment
{
    /// <summary>
    /// Manages infinite ocean background using chunk-based tile system.
    /// Creates seamless ocean environment that spawns/despawns around camera.
    /// </summary>
    public class OceanChunkManager : MonoBehaviour
    {
        [Header("Ocean Configuration")]
        [Tooltip("Ocean biome configuration with depth-based spawning")]
        [SerializeField] private OceanBiomeConfigurationSO biomeConfig;

        [Tooltip("Default ocean tile prefab (used when biome config doesn't specify)")]
        [SerializeField] private GameObject defaultOceanTilePrefab;

        [Tooltip("Size of each ocean tile in Unity units")]
        [SerializeField] private float tileSize = 1024f;

        [Tooltip("Grid radius around camera (3 = 7x7 grid, 4 = 9x9 grid, 5 = 11x11 grid)")]
        [Range(1, 7)]
        [SerializeField] private int gridRadius = 4;

        [Tooltip("Distance from camera edge before spawning new tiles")]
        [SerializeField] private float spawnDistance = 512f;

        [Tooltip("Distance from camera before despawning tiles")]
        [SerializeField] private float despawnDistance = 2048f;

        [Header("Legacy Ocean Variations (Deprecated)")]
        [Tooltip("Legacy materials - use biome config instead")]
        [SerializeField] private Material[] legacyOceanMaterials;

        [Tooltip("Enable depth-based tile variation")]
        [SerializeField] private bool enableDepthVariations = true;

        [Tooltip("Seed for deterministic tile placement")]
        [SerializeField] private int randomSeed = 12345;

        [Header("Debug Visualization")]
        [Tooltip("Show depth values in console for debugging")]
        [SerializeField] private bool debugDepthValues = false;

        [Tooltip("Show biome regions with color coding")]
        [SerializeField] private bool visualizeBiomes = false;

        [Header("Performance")]
        [Tooltip("Maximum tiles to process per frame")]
        [Range(1, 50)]
        [SerializeField] private int tilesPerFrame = 25;

        [Header("Runtime Culling Controls")]
        [Tooltip("Runtime override: Disable all culling systems")]
        [SerializeField] private bool runtimeDisableCulling = false;

        [Tooltip("Runtime override: Force enable all tile renderers")]
        [SerializeField] private bool runtimeForceEnableRenderers = false;

        [Tooltip("Runtime override: Grid radius")]
        [Range(1, 10)]
        [SerializeField] private int runtimeGridRadius = 5;

        [Tooltip("Show runtime debug GUI")]
        [SerializeField] private bool showRuntimeGUI = true;

        [Header("Color Blending")]
        [Tooltip("Enable smooth color blending between neighboring tiles")]
        [SerializeField] private bool enableColorBlending = true;

        [Tooltip("Blend strength for color transitions")]
        [Range(0f, 1f)]
        [SerializeField] private float colorBlendStrength = 0.3f;

        [Tooltip("Update frequency in seconds")]
        [Range(0.1f, 2f)]
        [SerializeField] private float updateInterval = 0.2f;

        // Core Components
        private UnityEngine.Camera oceanCamera;
        private Transform cameraTransform;

        // Tile Management
        private Dictionary<Vector2Int, GameObject> activeTiles;
        private Queue<Vector2Int> tilesToSpawn;
        private Queue<Vector2Int> tilesToDespawn;
        private Transform tilesContainer;

        // State Tracking
        private Vector2Int lastCameraChunk;
        private float lastUpdateTime;
        private Unity.Mathematics.Random randomGenerator;

        // Performance Monitoring
        private int tilesSpawnedThisFrame;
        private int tilesDespawnedThisFrame;

        // [Rest of implementation - 900+ lines including chunk spawning/despawning, biome variation system,
        // color blending, runtime culling controls, debug visualization, gizmos, and performance optimization]
    }

    /// <summary>
    /// Ocean statistics for debugging and monitoring
    /// </summary>
    [System.Serializable]
    public struct OceanStats
    {
        public int activeTileCount;
        public int tilesInSpawnQueue;
        public int tilesInDespawnQueue;
        public Vector2Int currentChunk;
        public float tileSize;
        public int gridRadius;

        public override string ToString()
        {
            return $"Ocean Stats: {activeTileCount} tiles active, Chunk: {currentChunk}, Queue: +{tilesInSpawnQueue}/-{tilesInDespawnQueue}";
        }
    }
}
