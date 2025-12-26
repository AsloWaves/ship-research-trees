# EquipmentDatabaseSOEditor.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Editor/EquipmentDatabaseSOEditor.cs` |
| **Namespace** | `WOS.Editor` |
| **Inheritance** | `UnityEditor.Editor` |
| **Lines** | 391 |
| **Architecture** | Custom Editor for Equipment Database Management |

## Purpose

Custom Unity Editor for `EquipmentDatabaseSO` that provides database management tools, validation, and statistics for equipment collections (turrets, torpedoes, modules). Enables auto-population from project assets, database validation, and comprehensive statistics with nation/tier breakdowns.

## Key Features

### Database Management
- **Auto-Population**: Find and add all equipment assets automatically
- **Selective Search**: Find specific equipment types (turrets, torpedoes, modules)
- **Null Cleanup**: Remove missing/deleted asset references
- **Validation**: Comprehensive database integrity checks

### Statistics & Analytics
- **Category Breakdown**: Equipment counts by category
- **Nation Analysis**: Equipment distribution by nation
- **Tier Analysis**: Turret distribution by tier
- **Total Counts**: Quick overview of database size

### Quality Assurance
- **Validation Reports**: Errors and warnings with detailed messages
- **Duplicate Detection**: Find duplicate equipment entries
- **Missing Reference Detection**: Identify null entries
- **Completeness Checks**: Verify required fields populated

## Configuration Tables

### Quick Actions
| Button | Function | Description |
|--------|----------|-------------|
| Validate Database | Run validation | Check for errors and warnings |
| Update Stats | Recalculate stats | Refresh category/nation/tier counts |
| Find All Turrets | Auto-populate | Search for TurretDefinitionSO assets |
| Find All Torpedoes | Auto-populate | Search for TorpedoDefinitionSO assets |
| Find All Modules | Auto-populate | Search for ModuleDefinitionSO assets |
| Auto-Populate All | Full auto-populate | Find and add all equipment types |

### Turret Categories
| Category | Description |
|----------|-------------|
| AntiAircraft | AA guns |
| DualPurpose | Surface and air |
| MainGun | Primary armament |
| SecondaryGun | Auxiliary batteries |
| Torpedo | Torpedo launchers |

### Validation Report Levels
| Level | Icon | Action |
|-------|------|--------|
| Error | ! | Critical issues requiring fixes |
| Warning | ⚠ | Non-critical issues, recommend review |
| Info | i | Informational messages |

## Key Code Snippets

### Database Header Display
```csharp
private void DrawDatabaseHeader()
{
    EditorGUILayout.BeginVertical(EditorStyles.helpBox);

    GUIStyle headerStyle = new GUIStyle(EditorStyles.boldLabel)
    {
        fontSize = 14,
        alignment = TextAnchor.MiddleCenter
    };

    EditorGUILayout.LabelField("Equipment Database", headerStyle);

    int turretCount = database.turrets?.Count(t => t != null) ?? 0;
    int torpedoCount = database.torpedoes?.Count(t => t != null) ?? 0;
    int moduleCount = database.modules?.Count(m => m != null) ?? 0;
    int total = turretCount + torpedoCount + moduleCount;

    EditorGUILayout.LabelField($"Total Equipment: {total} ({turretCount} Turrets, {torpedoCount} Torpedoes, {moduleCount} Modules)",
        EditorStyles.centeredGreyMiniLabel);

    EditorGUILayout.EndVertical();
}
```

**Purpose**: Displays database summary with total equipment counts by type.

### Auto-Populate All Equipment
```csharp
private void AutoPopulateDatabase()
{
    int totalAdded = 0;

    // Find turrets
    string[] turretGuids = AssetDatabase.FindAssets("t:TurretDefinitionSO");
    foreach (string guid in turretGuids)
    {
        string path = AssetDatabase.GUIDToAssetPath(guid);
        var turret = AssetDatabase.LoadAssetAtPath<TurretDefinitionSO>(path);
        if (turret != null && !database.turrets.Contains(turret))
        {
            database.turrets.Add(turret);
            totalAdded++;
        }
    }

    // Find torpedoes
    string[] torpedoGuids = AssetDatabase.FindAssets("t:TorpedoDefinitionSO");
    foreach (string guid in torpedoGuids)
    {
        string path = AssetDatabase.GUIDToAssetPath(guid);
        var torpedo = AssetDatabase.LoadAssetAtPath<TorpedoDefinitionSO>(path);
        if (torpedo != null && !database.torpedoes.Contains(torpedo))
        {
            database.torpedoes.Add(torpedo);
            totalAdded++;
        }
    }

    // Find modules
    string[] moduleGuids = AssetDatabase.FindAssets("t:ModuleDefinitionSO");
    foreach (string guid in moduleGuids)
    {
        string path = AssetDatabase.GUIDToAssetPath(guid);
        var module = AssetDatabase.LoadAssetAtPath<ModuleDefinitionSO>(path);
        if (module != null && !database.modules.Contains(module))
        {
            database.modules.Add(module);
            totalAdded++;
        }
    }

    // Remove nulls
    database.turrets.RemoveAll(t => t == null);
    database.torpedoes.RemoveAll(t => t == null);
    database.modules.RemoveAll(m => m == null);

    database.UpdateStats();
    EditorUtility.SetDirty(database);

    EditorUtility.DisplayDialog("Auto-Populate",
        $"Added {totalAdded} new equipment entries.\\n\\n" +
        $"Turrets: {database.turrets.Count}\\n" +
        $"Torpedoes: {database.torpedoes.Count}\\n" +
        $"Modules: {database.modules.Count}", "OK");
}
```

**Purpose**: Searches entire project for equipment assets and adds them to database, skipping duplicates.

### Statistics Display
```csharp
private void DrawStatistics()
{
    EditorGUILayout.BeginVertical(EditorStyles.helpBox);
    EditorGUILayout.LabelField("Statistics", EditorStyles.boldLabel);

    // Turret stats
    showTurretStats = EditorGUILayout.Foldout(showTurretStats, $"Turrets ({database.turrets?.Count(t => t != null) ?? 0})");
    if (showTurretStats && database.turrets != null)
    {
        EditorGUI.indentLevel++;

        // By Category
        var byCategory = database.turrets
            .Where(t => t != null)
            .GroupBy(t => t.turretCategory)
            .OrderBy(g => g.Key);

        foreach (var group in byCategory)
        {
            EditorGUILayout.LabelField($"{group.Key}: {group.Count()}");
        }

        EditorGUI.indentLevel--;
    }

    // Nation breakdown
    showNationBreakdown = EditorGUILayout.Foldout(showNationBreakdown, "By Nation");
    if (showNationBreakdown)
    {
        EditorGUI.indentLevel++;
        var nationCounts = database.GetEquipmentCountByNation();
        foreach (var kvp in nationCounts.Where(n => n.Value > 0))
        {
            EditorGUILayout.LabelField($"{kvp.Key}: {kvp.Value}");
        }
        EditorGUI.indentLevel--;
    }

    // Tier breakdown
    showTierBreakdown = EditorGUILayout.Foldout(showTierBreakdown, "By Tier");
    if (showTierBreakdown)
    {
        EditorGUI.indentLevel++;
        var tierCounts = database.GetTurretCountByTier();
        foreach (var kvp in tierCounts.Where(t => t.Value > 0))
        {
            EditorGUILayout.LabelField($"Tier {kvp.Key}: {kvp.Value}");
        }
        EditorGUI.indentLevel--;
    }

    EditorGUILayout.EndVertical();
}
```

**Purpose**: Displays collapsible statistics with category, nation, and tier breakdowns.

### Validation Display
```csharp
private void DrawValidationSection()
{
    showValidation = EditorGUILayout.Foldout(showValidation, "Validation Results");
    if (!showValidation) return;

    EditorGUILayout.BeginVertical(EditorStyles.helpBox);

    if (lastReport == null)
    {
        EditorGUILayout.HelpBox("Click 'Validate Database' to check for issues.", MessageType.Info);
    }
    else
    {
        // Show status
        if (lastReport.HasErrors)
        {
            EditorGUILayout.HelpBox($"{lastReport.errors.Count} errors found!", MessageType.Error);
        }
        else if (lastReport.HasWarnings)
        {
            EditorGUILayout.HelpBox($"No errors. {lastReport.warnings.Count} warnings.", MessageType.Warning);
        }
        else
        {
            EditorGUILayout.HelpBox("Database is valid!", MessageType.Info);
        }

        // Show errors
        if (lastReport.errors.Count > 0)
        {
            EditorGUILayout.LabelField("Errors:", EditorStyles.boldLabel);
            scrollPosition = EditorGUILayout.BeginScrollView(scrollPosition, GUILayout.MaxHeight(100));
            foreach (var error in lastReport.errors)
            {
                EditorGUILayout.BeginHorizontal();
                EditorGUILayout.LabelField("!", GUILayout.Width(15));
                EditorGUILayout.LabelField(error, EditorStyles.wordWrappedMiniLabel);
                EditorGUILayout.EndHorizontal();
            }
            EditorGUILayout.EndScrollView();
        }

        // Show warnings (limited to 20 displayed)
        if (lastReport.warnings.Count > 0)
        {
            EditorGUILayout.LabelField($"Warnings ({lastReport.warnings.Count}):", EditorStyles.boldLabel);
            scrollPosition = EditorGUILayout.BeginScrollView(scrollPosition, GUILayout.MaxHeight(150));
            foreach (var warning in lastReport.warnings.Take(20))
            {
                EditorGUILayout.BeginHorizontal();
                EditorGUILayout.LabelField("⚠", GUILayout.Width(15));
                EditorGUILayout.LabelField(warning, EditorStyles.wordWrappedMiniLabel);
                EditorGUILayout.EndHorizontal();
            }
            if (lastReport.warnings.Count > 20)
            {
                EditorGUILayout.LabelField($"... and {lastReport.warnings.Count - 20} more");
            }
            EditorGUILayout.EndScrollView();
        }
    }

    EditorGUILayout.EndVertical();
}
```

**Purpose**: Displays validation results with scrollable error/warning lists.

### Generic Equipment Finder
```csharp
private void FindAndAddEquipment<T>(string typeName) where T : EquipmentDefinitionSO
{
    string[] guids = AssetDatabase.FindAssets($"t:{typeof(T).Name}");
    int added = 0;

    foreach (string guid in guids)
    {
        string path = AssetDatabase.GUIDToAssetPath(guid);
        T equipment = AssetDatabase.LoadAssetAtPath<T>(path);

        if (equipment != null)
        {
            if (typeof(T) == typeof(TurretDefinitionSO))
            {
                if (!database.turrets.Contains(equipment as TurretDefinitionSO))
                {
                    database.turrets.Add(equipment as TurretDefinitionSO);
                    added++;
                }
            }
            else if (typeof(T) == typeof(TorpedoDefinitionSO))
            {
                if (!database.torpedoes.Contains(equipment as TorpedoDefinitionSO))
                {
                    database.torpedoes.Add(equipment as TorpedoDefinitionSO);
                    added++;
                }
            }
            else if (typeof(T) == typeof(ModuleDefinitionSO))
            {
                if (!database.modules.Contains(equipment as ModuleDefinitionSO))
                {
                    database.modules.Add(equipment as ModuleDefinitionSO);
                    added++;
                }
            }
        }
    }

    EditorUtility.SetDirty(database);
    EditorUtility.DisplayDialog("Find Equipment",
        $"Found {guids.Length} {typeName} assets.\\nAdded {added} new entries.", "OK");
}
```

**Purpose**: Generic method to find and add specific equipment types with duplicate prevention.

## Public API

### Unity Menu Items
None - this is a CustomEditor that appears automatically in the Inspector when an `EquipmentDatabaseSO` asset is selected.

### Inspector Actions
See Quick Actions table above.

## Usage Examples

### Initial Database Setup
1. Create database asset: `Create > WOS > Database > Equipment Database`
2. Select asset in Project window
3. In Inspector, click "Auto-Populate All Equipment"
4. Wait for search to complete (displays dialog with results)
5. Click "Validate Database" to check for issues
6. Review validation results and fix any errors

### Adding New Equipment
**Option 1 - Automatic**:
1. Create new equipment asset (turret/torpedo/module)
2. Select Equipment Database asset
3. Click "Auto-Populate All Equipment" to refresh
4. Database automatically finds and adds new assets

**Option 2 - Selective**:
1. Select Equipment Database asset
2. Click "Find All Turrets" (or specific type)
3. Only that equipment type is scanned and added

**Option 3 - Manual**:
1. Select Equipment Database asset
2. Expand "Turrets" (or other category) in default inspector
3. Click "+" to add array element
4. Drag equipment asset into slot

### Database Validation Workflow
```csharp
// Programmatic validation (for testing)
var database = AssetDatabase.LoadAssetAtPath<EquipmentDatabaseSO>("Assets/Resources/Databases/EquipmentDatabase.asset");
var report = database.ValidateDatabase();

if (report.HasErrors)
{
    Debug.LogError($"Database has {report.errors.Count} errors!");
    foreach (var error in report.errors)
    {
        Debug.LogError(error);
    }
}
```

### Removing Deleted Assets
1. Select Equipment Database asset
2. Click "Auto-Populate All Equipment"
3. Database automatically removes null entries
4. Check validation results for any remaining issues

## Integration Points

### Dependencies
- **EquipmentDatabaseSO**: The ScriptableObject being edited
- **TurretDefinitionSO**: Turret equipment assets
- **TorpedoDefinitionSO**: Torpedo equipment assets
- **ModuleDefinitionSO**: Module equipment assets
- **ValidationReport**: Validation result data structure

### Related Systems
- **TurretDefinitionSOEditor**: Creates turret assets added to database
- **TorpedoDefinitionSOEditor**: Creates torpedo assets added to database
- **ShipDefinitionSOEditor**: References database for ship loadouts
- **Inventory System**: Uses database for equipment catalog
- **Economy System**: References database for equipment pricing

### Data Flow
```
Equipment Editors (TurretDefinitionSOEditor, etc.)
    → Individual Equipment Assets (TurretDefinitionSO, etc.)
    → EquipmentDatabaseSOEditor (collection management)
    → EquipmentDatabaseSO (centralized database)
    → Runtime Systems (Inventory, Economy, Ship Loadouts)
```

## Design Notes

### Architectural Decisions
- **Centralized Database**: Single source of truth for all equipment
- **Auto-Population**: Reduces manual maintenance burden
- **Validation System**: Proactive quality assurance
- **Statistics Display**: Quick overview of database contents
- **Generic Methods**: Code reuse for equipment type operations

### Performance Considerations
- AssetDatabase searches cached during editor session
- Statistics calculated on-demand (not every frame)
- Validation runs only when requested
- Large databases may take seconds to populate

### Database Integrity
- Duplicate prevention during auto-population
- Null reference cleanup
- Validation reports missing required fields
- Statistics update after modifications

### Limitations
- No undo support for auto-populate operations
- Validation limited to 20 displayed warnings (performance)
- No batch delete functionality
- No import/export to external formats
- Statistics don't include module breakdowns

### Future Enhancements
- Export database to JSON/CSV
- Import equipment from external data
- Batch operations (delete, modify)
- Advanced filtering (nation, tier, category)
- Equipment comparison tools
- Duplicate detection and merging
- Equipment templates and cloning
- Version control and migration tools
- Module statistics breakdown
- Equipment dependency graph

### Common Patterns
- All modifications trigger `EditorUtility.SetDirty()`
- Results displayed in `EditorUtility.DisplayDialog()`
- LINQ used for category/nation/tier grouping
- Null-safe operations throughout (`?.`, `??`)
- Foldout sections for organized UI

### Debugging Tips
- Check console for validation errors
- Use "Update Stats" to refresh after manual changes
- "Auto-Populate" is safe to run repeatedly
- Validation warnings may be informational only
- Large databases may have performance impact
- Check for null references in individual equipment assets
- Verify equipment assets are in correct namespace
