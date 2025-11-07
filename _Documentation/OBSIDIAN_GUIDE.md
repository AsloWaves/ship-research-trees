# Obsidian Optimization Guide

Quick reference for using this repository with Obsidian Canvas and research workflows.

## Directory Structure for Obsidian

This repository is organized by **TYPE** (Ships, Aircraft, Weapons) with research trees kept alongside their content:

```
Ships/[Nation]/[Type]/         → Individual ship classes
Ships/[Nation]/Overviews/      → Research trees for that nation
Aircraft/Research-Trees/       → Aircraft research trees
Weapons/[Type]/Research-Trees/ → Weapons research trees
```

## Canvas Workflow

### Creating Research Tree Canvases
1. Create new Canvas in `.obsidian/canvas/`
2. Link to research tree markdown: `Ships/USA/Overviews/00_Battleship_Research_Tree.md`
3. Add individual ship class cards by linking to ship files
4. Arrange by tier/generation/relationship

### Best Practices
- Keep research trees in markdown (Canvas consumes them)
- Use Canvas for visual relationship mapping
- Link liberally between related classes

## Linking Conventions

- Ship classes: `[[Ship-Class-Name]]`
- Aircraft: `[[Designation]]` (e.g., `[[F4U-1 Corsair]]`)
- Weapons: `[[Weapon-Designation]]`
- Research trees: `[[00_Battleship_Research_Tree]]`

## YAML Frontmatter

All ship/aircraft markdown files include metadata:
```yaml
---
designation: Iowa-Class
nation: USA
type: Battleship
commissioned: 1943
decommissioned: 1992
tags: [battleship, fast-battleship, iowa-class]
---
```

Use Dataview queries to filter/search by these fields.

## Quick Tips

1. **Research Trees Stay With Content** - Find battleship trees in `Ships/[Nation]/Overviews/`, not a central location
2. **Archive is Hidden** - `_Archive/`, `_Scripts/`, `_Documentation/` are supporting directories, not primary research
3. **Databases Are Secondary** - Markdown files are the source of truth for ships; databases for complex queries only
4. **Aircraft Needs Work** - Aircraft data currently in database only, markdown generation needed

## Future Enhancements

- Dataview queries for ship statistics
- Templater templates for new ship classes
- Canvas templates for standard research tree layouts
- Cross-linking between ships and their weapons
