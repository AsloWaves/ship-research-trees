# ResearchImporter.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Editor/ResearchImporter.cs` |
| **Namespace** | `WOS.Editor` |
| **Inheritance** | `UnityEditor.EditorWindow` |
| **Lines** | 625 |
| **Architecture** | Bulk Import EditorWindow with Multi-Format Parsing |

## Purpose

Unity Editor Window for bulk importing research nodes from CSV, JSON, or Markdown files into ResearchNodeSO ScriptableObjects. Automates creation of research tree assets with support for automatic prerequisite linking, folder organization by nation/tier, and batch asset generation. Accessible via `Window > WOS > Research Importer`.

## Key Features

### Multi-Format Import
- **CSV Support**: Comma-separated values with header row
- **JSON Support**: Array of research node objects
- **Markdown Support**: Table format extraction from markdown files
- **Template Generation**: Auto-generate example import files

### Automation
- **Auto-Prerequisite Linking**: Links research nodes based on tier progression or explicit IDs
- **Folder Organization**: Hierarchical folder structure by Nation/Tier
- **Batch Creation**: Create hundreds of research nodes in seconds
- **Update Existing**: Updates existing assets instead of creating duplicates

### Quality Assurance
- **Import Logging**: Detailed log output for debugging
- **Error Handling**: Graceful error recovery with detailed messages
- **Validation**: Checks for missing columns, invalid data
- **Progress Feedback**: Real-time import status

## Configuration Tables

### Import Format Support
| Format | File Extensions | Parsing Method |
|--------|----------------|----------------|
| CSV | .csv, .txt | `ParseCSV()` |
| JSON | .json | `ParseJSON()` |
| Markdown | .md | `ParseMarkdown()` |

### CSV Column Schema
| Column | Type | Required | Description |
|--------|------|----------|-------------|
| nodeId | string | Yes | Unique identifier (e.g., "usa_bb_t5") |
| nodeName | string | Yes | Display name (e.g., "Iowa-class") |
| description | string | Yes | Tooltip description |
| researchType | enum | No | Ship, Equipment, Skill, etc. |
| nation | enum | No | USA, Japan, Germany, etc. |
| tier | int | No | 1-10 tier level |
| unlockType | enum | No | Ship, Module, Crew, etc. |
| researchXP | long | No | XP cost to research |
| researchCredits | int | No | Credit cost to research |
| researchTime | int | No | Time in seconds (0 = instant) |
| minPlayerLevel | int | No | Required player level |
| gridX | int | No | Canvas X position |
| gridY | int | No | Canvas Y position |
| canvasId | string | No | Obsidian Canvas node ID |
| prerequisiteIds | string | No | Semicolon-separated node IDs |

### Folder Organization Patterns
| Organize By Nation | Organize By Tier | Result Path |
|-------------------|------------------|-------------|
| ✅ | ✅ | `Output/USA/Tier5/ResearchNode_usa_bb_t5.asset` |
| ✅ | ❌ | `Output/USA/ResearchNode_usa_bb_t5.asset` |
| ❌ | ✅ | `Output/Tier5/ResearchNode_usa_bb_t5.asset` |
| ❌ | ❌ | `Output/ResearchNode_usa_bb_t5.asset` |

### Prerequisite Linking Modes
| Mode | Description | Trigger |
|------|-------------|---------|
| Explicit | Links based on prerequisiteIds column | Data contains prerequisite IDs |
| Tier-Based | Auto-links based on tier progression | No explicit prerequisites |
| None | No automatic linking | Auto-Link Prerequisites disabled |

## Key Code Snippets

### Main Import Logic
```csharp
private void ImportResearchNodes()
{
    importLog = $"Starting import from: {importFilePath}\n";
    importLog += $"Format: {importFormat}\n\n";

    try
    {
        List<ResearchNodeData> nodeData = null;

        switch (importFormat)
        {
            case ImportFormat.CSV:
                nodeData = ParseCSV(importFilePath);
                break;
            case ImportFormat.JSON:
                nodeData = ParseJSON(importFilePath);
                break;
            case ImportFormat.Markdown:
                nodeData = ParseMarkdown(importFilePath);
                break;
        }

        if (nodeData == null || nodeData.Count == 0)
        {
            importLog += "ERROR: No data parsed from file!\n";
            return;
        }

        importLog += $"Parsed {nodeData.Count} nodes from file.\n\n";

        // Create ScriptableObjects
        List<ResearchNodeSO> createdNodes = CreateResearchNodes(nodeData);

        importLog += $"Created {createdNodes.Count} ResearchNodeSO assets.\n\n";

        // Auto-link prerequisites
        if (autoLinkPrerequisites)
        {
            LinkPrerequisites(createdNodes, nodeData);
            importLog += "Prerequisite linking complete.\n\n";
        }

        importLog += "Import complete!\n";
        AssetDatabase.SaveAssets();
        AssetDatabase.Refresh();
    }
    catch (Exception ex)
    {
        importLog += $"ERROR: {ex.Message}\n";
        importLog += $"Stack Trace: {ex.StackTrace}\n";
    }
}
```

**Purpose**: Main import workflow that parses data, creates assets, and links prerequisites.

### CSV Parsing with Robust Error Handling
```csharp
private List<ResearchNodeData> ParseCSV(string filePath)
{
    List<ResearchNodeData> nodes = new List<ResearchNodeData>();

    string[] lines = File.ReadAllLines(filePath);
    if (lines.Length < 2)
    {
        importLog += "ERROR: CSV file has no data rows!\n";
        return nodes;
    }

    // Parse header
    string[] headers = lines[0].Split(',');
    importLog += $"CSV Headers: {string.Join(", ", headers)}\n";

    // Parse data rows
    for (int i = 1; i < lines.Length; i++)
    {
        string line = lines[i].Trim();
        if (string.IsNullOrEmpty(line))
            continue;

        string[] values = line.Split(',');
        if (values.Length < 3)
        {
            importLog += $"Skipping line {i + 1}: Not enough columns\n";
            continue;
        }

        try
        {
            var nodeData = new ResearchNodeData
            {
                nodeId = values.Length > 0 ? values[0].Trim().Trim('"') : "",
                nodeName = values.Length > 1 ? values[1].Trim().Trim('"') : "",
                description = values.Length > 2 ? values[2].Trim().Trim('"') : "",
                researchType = values.Length > 3 ? ParseEnum<ResearchType>(values[3].Trim('"')) : ResearchType.Ship,
                nation = values.Length > 4 ? ParseEnum<ResearchNation>(values[4].Trim('"')) : ResearchNation.USA,
                tier = values.Length > 5 ? ParseInt(values[5].Trim('"'), 1) : 1,
                // ... additional columns ...
            };

            // Parse prerequisites (column 14, semicolon-separated)
            if (values.Length > 14 && !string.IsNullOrEmpty(values[14].Trim()))
            {
                string prereqString = values[14].Trim().Trim('"');
                if (!string.IsNullOrEmpty(prereqString))
                {
                    string[] prereqIds = prereqString.Split(';');
                    nodeData.prerequisiteIds = prereqIds.Select(p => p.Trim()).Where(p => !string.IsNullOrEmpty(p)).ToList();
                }
            }

            nodes.Add(nodeData);
        }
        catch (Exception ex)
        {
            importLog += $"Error parsing line {i + 1}: {ex.Message}\n";
        }
    }

    return nodes;
}
```

**Purpose**: Parses CSV files with error recovery, handling quoted strings and missing columns.

### ScriptableObject Creation with Folder Organization
```csharp
private List<ResearchNodeSO> CreateResearchNodes(List<ResearchNodeData> nodeData)
{
    List<ResearchNodeSO> createdNodes = new List<ResearchNodeSO>();

    // Ensure output folder exists
    if (!AssetDatabase.IsValidFolder(outputFolder))
    {
        string[] folders = outputFolder.Split('/');
        string currentPath = folders[0];
        for (int i = 1; i < folders.Length; i++)
        {
            string newPath = currentPath + "/" + folders[i];
            if (!AssetDatabase.IsValidFolder(newPath))
            {
                AssetDatabase.CreateFolder(currentPath, folders[i]);
            }
            currentPath = newPath;
        }
    }

    foreach (var data in nodeData)
    {
        // Determine output path
        string assetPath = outputFolder;

        if (organizeByNation)
        {
            assetPath += "/" + data.nation.ToString();
            if (!AssetDatabase.IsValidFolder(assetPath))
            {
                AssetDatabase.CreateFolder(outputFolder, data.nation.ToString());
            }
        }

        if (organizeByTier)
        {
            string tierFolder = assetPath + "/Tier" + data.tier;
            if (!AssetDatabase.IsValidFolder(tierFolder))
            {
                string parentFolder = organizeByNation ? (outputFolder + "/" + data.nation.ToString()) : outputFolder;
                AssetDatabase.CreateFolder(parentFolder, "Tier" + data.tier);
            }
            assetPath = tierFolder;
        }

        // Create asset
        string fileName = $"ResearchNode_{data.nodeId}.asset";
        string fullPath = assetPath + "/" + fileName;

        // Check if already exists
        ResearchNodeSO existingNode = AssetDatabase.LoadAssetAtPath<ResearchNodeSO>(fullPath);
        ResearchNodeSO node;

        if (existingNode != null)
        {
            node = existingNode;
            importLog += $"Updating existing: {fileName}\n";
        }
        else
        {
            node = ScriptableObject.CreateInstance<ResearchNodeSO>();
            AssetDatabase.CreateAsset(node, fullPath);
            importLog += $"Created: {fileName}\n";
        }

        // Set properties
        node.nodeId = data.nodeId;
        node.nodeName = data.nodeName;
        node.description = data.description;
        // ... set all properties ...
        node.isStartingNode = (data.tier == 1);

        EditorUtility.SetDirty(node);
        createdNodes.Add(node);
    }

    return createdNodes;
}
```

**Purpose**: Creates or updates ResearchNodeSO assets with hierarchical folder organization.

### Auto-Prerequisite Linking
```csharp
private void LinkPrerequisites(List<ResearchNodeSO> nodes, List<ResearchNodeData> nodeData = null)
{
    // Create lookup dictionary (nodeId -> ResearchNodeSO)
    Dictionary<string, ResearchNodeSO> nodeLookup = new Dictionary<string, ResearchNodeSO>();
    foreach (var node in nodes)
    {
        if (!nodeLookup.ContainsKey(node.nodeId))
        {
            nodeLookup[node.nodeId] = node;
        }
    }

    // If we have explicit prerequisites from CSV/Canvas, use those first
    if (nodeData != null)
    {
        importLog += "Linking explicit prerequisites from import data...\n";

        for (int i = 0; i < nodeData.Count && i < nodes.Count; i++)
        {
            var data = nodeData[i];
            var node = nodes[i];

            if (data.prerequisiteIds != null && data.prerequisiteIds.Count > 0)
            {
                foreach (var prereqId in data.prerequisiteIds)
                {
                    if (nodeLookup.TryGetValue(prereqId, out ResearchNodeSO prereqNode))
                    {
                        if (!node.prerequisiteNodes.Contains(prereqNode))
                        {
                            node.prerequisiteNodes.Add(prereqNode);
                            EditorUtility.SetDirty(node);
                            importLog += $"  Linked {node.nodeName} → {prereqNode.nodeName} (explicit)\n";
                        }
                    }
                    else
                    {
                        importLog += $"  WARNING: Prerequisite '{prereqId}' not found for {node.nodeName}\n";
                    }
                }
            }
        }
    }
    else
    {
        // Fallback: Auto-link based on tier progression
        importLog += "Auto-linking based on tier progression...\n";

        var groups = nodes.GroupBy(n => new { n.nation, n.researchType });

        foreach (var group in groups)
        {
            var sortedNodes = group.OrderBy(n => n.tier).ToList();

            for (int i = 1; i < sortedNodes.Count; i++)
            {
                var currentNode = sortedNodes[i];
                var previousNode = sortedNodes[i - 1];

                // Link to previous tier
                if (currentNode.tier == previousNode.tier + 1)
                {
                    if (!currentNode.prerequisiteNodes.Contains(previousNode))
                    {
                        currentNode.prerequisiteNodes.Add(previousNode);
                        EditorUtility.SetDirty(currentNode);
                        importLog += $"  Linked {currentNode.nodeName} → {previousNode.nodeName} (tier-based)\n";
                    }
                }
            }
        }
    }
}
```

**Purpose**: Links research nodes either by explicit prerequisite IDs or automatic tier progression.

### CSV Template Generation
```csharp
private void GenerateCSVTemplate()
{
    string templatePath = EditorUtility.SaveFilePanel("Save CSV Template", Application.dataPath, "research_template.csv", "csv");
    if (string.IsNullOrEmpty(templatePath))
        return;

    string csv = "nodeId,nodeName,description,researchType,nation,tier,unlockType,researchXP,researchCredits,researchTime,minPlayerLevel,gridX,gridY\n";
    csv += "usa_bb_t1,Wyoming-class,First battleship,Ship,USA,1,Ship,500,5000,0,1,0,0\n";
    csv += "usa_bb_t3,New Mexico-class,Mid-tier battleship,Ship,USA,3,Ship,25000,150000,3600,15,2,0\n";
    csv += "usa_bb_t5,Iowa-class,Fast battleship,Ship,USA,5,Ship,250000,1500000,14400,30,4,0\n";

    File.WriteAllText(templatePath, csv);
    importLog = $"CSV template created at: {templatePath}\n";
}
```

**Purpose**: Generates example CSV template with sample battleship research nodes.

## Public API

### Unity Menu Items
| Menu Path | Function |
|-----------|----------|
| `Window > WOS > Research Importer` | Open importer window |

### EditorWindow Controls
| Control | Type | Function |
|---------|------|----------|
| File Path | TextField + Browse | Select import file |
| Import Format | Enum Popup | CSV, JSON, or Markdown |
| Output Folder | TextField + Browse | Asset output location |
| Auto-Link Prerequisites | Toggle | Enable prerequisite linking |
| Organize by Nation | Toggle | Create nation subfolders |
| Organize by Tier | Toggle | Create tier subfolders |
| Import Research Nodes | Button | Execute import |
| Generate CSV Template | Button | Create example CSV |
| Generate JSON Template | Button | Create example JSON |
| Import Log | TextArea | Display import status |

## Usage Examples

### Basic CSV Import
1. Open window: `Window > WOS > Research Importer`
2. Click "Generate CSV Template" to create example file
3. Edit CSV in Excel/Google Sheets with your research data
4. Click "Browse" next to "File Path" and select your CSV
5. Select "CSV" format
6. Set output folder: `Assets/ScriptableObjects/Research/Generated`
7. Enable "Auto-Link Prerequisites", "Organize by Nation", "Organize by Tier"
8. Click "Import Research Nodes"
9. Check Import Log for results

### CSV Format Example
```csv
nodeId,nodeName,description,researchType,nation,tier,unlockType,researchXP,researchCredits,researchTime,minPlayerLevel,gridX,gridY,prerequisiteIds
usa_bb_t1,Wyoming-class,First battleship,Ship,USA,1,Ship,500,5000,0,1,0,0,
usa_bb_t3,New Mexico-class,Mid-tier battleship,Ship,USA,3,Ship,25000,150000,3600,15,2,0,usa_bb_t1
usa_bb_t5,Iowa-class,Fast battleship,Ship,USA,5,Ship,250000,1500000,14400,30,4,0,usa_bb_t3
```

### JSON Import
1. Click "Generate JSON Template"
2. Edit JSON array with your data:
```json
[
  {
    "nodeId": "usa_bb_t5",
    "nodeName": "Iowa-class",
    "description": "Fast battleship",
    "researchType": "Ship",
    "nation": "USA",
    "tier": 5,
    "unlockType": "Ship",
    "researchXP": 250000,
    "researchCredits": 1500000,
    "researchTime": 14400,
    "minPlayerLevel": 30
  }
]
```
3. Select JSON format in importer
4. Import as normal

### Markdown Table Import
Create markdown file with table:
```markdown
# USA Battleships

| nodeId | nodeName | description | researchType | nation | tier |
|--------|----------|-------------|--------------|--------|------|
| usa_bb_t1 | Wyoming-class | First battleship | Ship | USA | 1 |
| usa_bb_t3 | New Mexico-class | Mid-tier battleship | Ship | USA | 3 |
| usa_bb_t5 | Iowa-class | Fast battleship | Ship | USA | 5 |
```

### Updating Existing Assets
1. Make changes to CSV/JSON/Markdown file
2. Re-run import with same output folder
3. Importer detects existing assets and updates them
4. Check log: "Updating existing: ResearchNode_usa_bb_t5.asset"

## Integration Points

### Dependencies
- **ResearchNodeSO**: The ScriptableObject type being created
- **UnityEditor.AssetDatabase**: For asset creation and folder management
- **System.IO.File**: For file reading
- **UnityEngine.JsonUtility**: For JSON parsing

### Related Systems
- **Research Tree UI**: Displays created research nodes
- **Progression System**: Uses research node data for unlocks
- **Economy System**: Uses research costs (XP, credits, time)
- **Player Progression**: Checks minPlayerLevel requirements

### Data Flow
```
External Data (CSV/JSON/Markdown)
    → ResearchImporter (parsing)
    → ResearchNodeData (intermediate)
    → CreateResearchNodes() (asset creation)
    → ResearchNodeSO (ScriptableObject assets)
    → LinkPrerequisites() (graph construction)
    → Runtime Research System (gameplay)
```

## Design Notes

### Architectural Decisions
- **Multi-Format Support**: Flexibility for different data sources
- **Template Generation**: Quick start for new users
- **Folder Organization**: Hierarchical structure for large datasets
- **Auto-Linking**: Reduces manual prerequisite configuration
- **Update vs Create**: Safe to re-import without duplicates

### Performance Considerations
- Imports hundreds of nodes in seconds
- AssetDatabase.Refresh() called once at end
- Batch SaveAssets() for efficiency
- Dictionary lookup for O(1) prerequisite linking

### Obsidian Canvas Integration
- **canvasId field**: Stores Obsidian Canvas node ID
- **prerequisiteIds**: Extracted from Canvas edge data
- **Future**: Direct .canvas file parsing

### Limitations
- CSV parsing doesn't handle embedded commas in quoted strings
- JSON must be valid Unity JsonUtility format (no nested arrays)
- Markdown only supports simple tables (no colspan/rowspan)
- No undo support for bulk imports
- Large imports (1000+) may be slow

### Future Enhancements
- Direct Obsidian Canvas (.canvas) parsing
- Excel (.xlsx) import support
- Import validation preview before creation
- Undo/redo support
- Progress bar for large imports
- Duplicate detection and merging
- Export research tree to CSV/JSON
- Batch edit existing nodes
- Visual prerequisite graph viewer
- Research tree validation (cycles, orphans)

### Common Patterns
- All asset modifications use `EditorUtility.SetDirty()`
- Folder creation checks `AssetDatabase.IsValidFolder()` first
- Error handling wraps all parsing in try-catch
- Import log provides detailed feedback
- Robust null checking and default values

### Debugging Tips
- Check Import Log for detailed error messages
- Verify CSV headers match expected schema
- Test with template files first
- Enable all organization options for clearer structure
- Check for missing prerequisite IDs in log warnings
- Verify enum values match exactly (case-sensitive)
- Use Generate Template buttons to see correct format
