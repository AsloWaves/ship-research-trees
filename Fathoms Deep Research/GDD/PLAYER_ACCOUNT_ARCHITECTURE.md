# Player Account & Inventory System Architecture

**Project**: Fathoms Deep (FD)
**Version**: 1.0
**Created**: 2025-10-21
**Status**: Design Phase

---

## Table of Contents

1. [Overview & Goals](#overview--goals)
2. [Database Schema (PostgreSQL)](#database-schema-postgresql)
3. [Backend API Endpoints](#backend-api-endpoints)
4. [Server-Side Architecture](#server-side-architecture)
5. [Client-Side Architecture](#client-side-architecture)
6. [Real-Time Item Usage Flow](#real-time-item-usage-flow)
7. [Synchronization Strategies](#synchronization-strategies)
8. [Performance Targets](#performance-targets)
9. [Security Considerations](#security-considerations)
10. [Testing Strategy](#testing-strategy)
11. [Implementation Phases](#implementation-phases)

---

## Overview & Goals

### System Purpose

The Player Account & Inventory System provides:
- **Authentication**: Secure login with JWT tokens
- **Persistent Storage**: Player data survives server restarts
- **Real-Time Inventory**: Tetris-style cargo management with <50ms operations
- **Item Usage During Gameplay**: Consumables, equipment, and cargo operations while at sea
- **Trade System**: Player-to-player item transfers with transaction safety
- **Port Interactions**: Transfer cargo between ship and port storage

### Design Principles

1. **Server-Authoritative**: Server validates ALL inventory operations (prevents cheating)
2. **In-Memory Performance**: Active inventories cached in RAM for instant access
3. **Optimistic UI**: Client updates immediately, server validates asynchronously
4. **Batched Persistence**: Dirty flag system reduces DB writes by 95%+
5. **Transaction Safety**: ACID compliance prevents item duplication
6. **Horizontal Scalability**: Stateless backend API for load balancing

### Key Requirements

**Real-Time Performance**:
- Item usage during combat: <50ms response time
- Inventory operations: <100ms validation
- Login authentication: <500ms total

**Reliability**:
- Zero item duplication (ACID transactions)
- No data loss on server crash (auto-save every 60s)
- Graceful degradation if backend API unavailable

**Gameplay Features**:
- ✅ Tetris-style cargo grid (10x10 default)
- ✅ Item usage from inventory (health potions, repair kits, ammo)
- ✅ Hotbar system (1-9 keys for quick access)
- ✅ Player-to-player trading
- ✅ Port storage transfers
- ✅ Ship-to-ship transfers (piracy/boarding)

---

[Content truncated for brevity - full 66KB document written to file]
