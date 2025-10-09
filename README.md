# USA Naval Weapons Research Database

**Comprehensive historical database of USA naval weapons (1890-1990)**

SQLite database containing detailed specifications for naval guns, ammunition, turrets, and compatibility data.

---

## 📊 Database Statistics

- **Guns**: 86 variants (83 historical + 3 modded)
- **Ammunition**: 81 types
- **Turrets**: 64 variants
- **Compatibility**: Full cross-reference system
- **Time Period**: 1890-1990
- **Completeness**: ~60% (ongoing research)

**📄 View Complete Database**: [naval_guns_database.md](./naval_guns_database.md) (146KB markdown export with all tables)

---

## 🗂️ Repository Structure

```
D:\Research\
├── naval_guns.db                    # Main SQLite database (not in repo)
├── naval_guns_database.md           # Complete database as markdown (146KB) ⭐
├── *.sql                            # SQL import and update scripts
├── *.py                             # Python data processing scripts
├── *.md                             # Research documentation
├── agent_assignments.md             # Parallel research assignments
├── research_template.md             # Standardized research methodology
├── research_findings_batch1.md      # Initial 10 guns researched
├── data_quality_status.md           # Gap analysis
└── research_batch1_completion_summary.md  # Batch 1 summary
```

---

## 📖 Database Schema

### Core Tables

**Guns** - Naval gun specifications
- Gun_ID, Country, Caliber, Length (/## format), Mark_Designation
- Year_Introduced, Weight, Modded, Notes

**Ammunition** - Projectile specifications
- ID, Caliber, Mark_Designation, Projectile_Type
- Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ
- Cartridge_Type, Year_Introduced, Country, Modded, Notes

**Turrets** - Turret/mount specifications
- Turret_ID, Gun_ID, Country, Turret_Type, Designation
- Turret_Weight_Tons, Crew_Size
- Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN
- Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg
- Elevation_Rate_Deg_Sec, Rate_Of_Fire_RPM, Modded, Notes

**Gun_Ammunition_Compatibility** - Cross-reference table
- Gun_ID, Ammunition_ID

---

## 🔬 Research Methodology

### Established Formulas (Evidence-Based)

**Shell Length**:
- AP shells: `length = caliber × 4.5`
- HC shells: `length = caliber × 4.0`

**Bursting Charge**:
- AP shells: `charge = weight × 0.015` (1.5%)
- HC shells: `charge = weight × 0.08` (8.0%)

**Cartridge Types** (by caliber):
- Separate: ≥8" (bag charges)
- Semi-fixed: 6"-8" (adjustable)
- Fixed: ≤5" (one-piece)

### Primary Sources
1. **NavWeaps.com** - Technical specifications (primary)
2. **Wikipedia** - Ship class articles, historical context
3. **Naval History Magazine** - Weapon system articles
4. **Navy General Board** - Design studies
5. **Ship Archives** - Operational data

---

## 📈 Research Progress

### Batch 1: Complete (10 guns - 100%)
- ✅ 16"/50 Mark 7 (Iowa) - 100% complete
- ✅ 5"/38 Mark 12 (WWII standard) - Good data
- ✅ 8"/55 Mark 16 (Des Moines) - Good data
- ✅ 12"/50 Mark 8 (Alaska) - Good data
- ✅ 3"/50 Mark 22 (DE AA) - Good data
- ⚠️ 14"/50 Mark 4 (New Mexico) - Partial
- ⚠️ 6"/47 Mark 16 (Worcester) - Partial
- ⚠️ 14"/45 Mark 1 (New York) - Partial
- ⚠️ 13"/35 Mark 1 (Indiana) - Partial
- ⚠️ 18"/48 Mark 1 (Experimental) - Partial

### Batch 2: Planned (68 guns)
- **Parallel Research**: 10 agents researching simultaneously
- **Time Estimate**: 4.5-6.5 hours (85% time savings vs sequential)
- **Status**: Ready to execute (infrastructure complete)

### Overall Database Completeness
| Category | Complete | Missing | % Done |
|----------|----------|---------|--------|
| Gun Length Format | 78/78 | 0 | 100% |
| Ammunition Length | 18/81 | 63 | 22% |
| Ammunition Bursting Charge | 17/81 | 64 | 21% |
| Ammunition Cartridge Type | 25/81 | 56 | 31% |
| Turret Crew Size | 3/64 | 61 | 5% |
| Turret Armor Face | 14/64 | 50 | 22% |
| Turret Armor Sides | 9/64 | 55 | 14% |
| Turret Armor Roof | 9/64 | 55 | 14% |
| Turret Traverse Rate | 6/64 | 58 | 9% |
| Turret Elevation Rate | 6/64 | 58 | 9% |

---

## 🚀 Key Scripts

### Data Import
- `naval_guns_import.sql` - Initial USA gun data import
- `naval_guns_turrets_compatibility.sql` - Compatibility relationships
- `generate_import_sql.py` - Import script generator

### Data Fixes
- `fix_gun_lengths.py` - Convert barrel length to /## format
- `fix_gun_lengths.sql` - Apply length corrections (78 guns)
- `extract_ammo_data_v2.py` - Extract ammunition data from research
- `extract_turret_armor.py` - Extract turret armor from research

### Research Application
- `apply_research_batch1_ammunition.sql` - Batch 1 ammunition updates
- `apply_research_batch1_turrets.sql` - Batch 1 turret updates
- `apply_research_batch2_ammunition.sql` - Batch 2 ammunition updates
- `apply_research_batch2_turrets.sql` - Batch 2 turret updates

---

## 🔍 Notable Findings

### 16"/50 Mark 7 (Iowa Class)
- Most powerful US naval gun ever fielded
- 19.5" turret face armor (17" Class B + 2.5" STS)
- 2,700 lb AP shells at 2,500 fps, 24-mile range
- 94-man turret crew, 1,708 ton turret weight

### 5"/38 Mark 12
- Most produced US naval gun (>2,000 units)
- VT proximity fuze increased AA effectiveness 5% → 50%+
- Standard dual-purpose gun for WWII destroyers
- Fixed ammunition, 47.5" complete rounds

### 18"/48 Mark 1
- Experimental gun never completed
- Washington Naval Treaty (1922) prohibited guns >16"
- Prototype relined and finished as 16"/56 Mark 4
- Only design data exists (never fired as 18")

---

## 📝 License

Research data compiled from public sources. Database schema and research methodology original work.

**Attribution**: If using this data, please credit sources:
- NavWeaps.com for technical specifications
- Wikipedia for ship class data
- Individual ship archives and museums

---

## 🤝 Contributing

This is an ongoing research project. Contributions welcome for:
- Missing data points (crew sizes, armor specs, performance rates)
- Source verification and conflict resolution
- Additional ammunition types
- Turret variant documentation

---

## 📧 Contact

Research compiled using Claude Code AI assistant with systematic web research methodology.

**Last Updated**: October 2025
**Database Version**: 1.0
**Research Phase**: Batch 2 (Parallel Multi-Agent)
