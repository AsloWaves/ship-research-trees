BEGIN {
    FS = "|"
    OFS = "|"
    print "# Converting missile research nodes to detailed database entries"
    print "# Estimating specifications based on type, year, and country"
}

/^\| [0-9]/ {
    # Extract fields
    gsub(/^[ \t]+|[ \t]+$/, "", $2)  # Node_ID
    gsub(/^[ \t]+|[ \t]+$/, "", $3)  # Nation
    gsub(/^[ \t]+|[ \t]+$/, "", $4)  # Designation
    gsub(/^[ \t]+|[ \t]+$/, "", $5)  # Year
    gsub(/^[ \t]+|[ \t]+$/, "", $6)  # Tech_Branch
    gsub(/^[ \t]+|[ \t]+$/, "", $7)  # Type (SAM, SSM, ASW, etc)

    missile_id = $2
    country = $3
    designation = $4
    year = $5
    tech_branch = $6
    missile_type = $7

    # Skip if not missile
    if (tech_branch != "Missiles") next

    # Initialize variables
    diameter = 0
    missile_length = 0
    weight = 0
    warhead = 0
    speed = 0
    range_nm = 0
    guidance = ""
    propulsion = ""
    targets = ""
    platform = ""

    # DIAMETER estimation (inches)
    if (missile_type == "SAM") {
        if (designation ~ /Talos|Sea Slug/) {
            diameter = 30  # Large early SAMs
        } else if (designation ~ /Terrier|Sea Dart|Standard ER|ERAM/) {
            diameter = 13.5  # Medium-range SAMs
        } else if (designation ~ /Tartar|Standard MR|Type 03|Type 07|Sea Viper|Aster/) {
            diameter = 13.5  # Standard MR diameter
        } else if (designation ~ /Sea Sparrow|ESSM|Sea Wolf|CAMM|Bloodhound/) {
            diameter = 8  # Point defense
        } else if (designation ~ /RAM|RIM-116/) {
            diameter = 5  # Rolling Airframe Missile
        } else if (designation ~ /IRIS-T|Type 91|Type 93/) {
            diameter = 6  # MANPADS adapted
        } else if (designation ~ /SM-3/) {
            diameter = 13.5  # Ballistic missile defense
        } else if (designation ~ /SM-6/) {
            diameter = 13.5  # Dual-role
        } else {
            diameter = 13.5  # Default SAM
        }
    } else if (missile_type == "SSM" || missile_type == "Cruise") {
        if (designation ~ /Tomahawk|TLAM|TASM|Storm Shadow|JASSM|CALCM|ACM|Gryphon/) {
            diameter = 20.4  # Cruise missile standard
        } else if (designation ~ /Harpoon|Exocet|SSM-1|Type 88|Type 90|Type 12/) {
            diameter = 13.5  # Anti-ship standard
        } else if (designation ~ /Regulus/) {
            diameter = 54  # Large early cruise
        } else if (designation ~ /Penguin|Sea Skua|Kormoran|IDAS/) {
            diameter = 11  # Helicopter/light ASM
        } else if (designation ~ /NSM|LRASM/) {
            diameter = 17.7  # Modern stealth ASM
        } else if (designation ~ /ASM-1|ASM-2|ASM-3/) {
            diameter = 13.5  # Japanese air-to-ship
        } else if (designation ~ /Martlet|Sea Venom/) {
            diameter = 7  # Light ASM
        } else if (designation ~ /JSOW/) {
            diameter = 13  # Glide weapon
        } else if (designation ~ /CPS|Hypersonic/) {
            diameter = 34.5  # Hypersonic strike
        } else {
            diameter = 13.5  # Default SSM
        }
    } else if (missile_type == "ASW") {
        if (designation ~ /ASROC|VL-ASROC|VLA|Type 07 VLA/) {
            diameter = 12.75  # ASROC standard
        } else if (designation ~ /Weapon Alpha|Mk 108|Mk 112|Mk 113/) {
            diameter = 7.2  # ASW rockets
        } else if (designation ~ /SUBROC|Sea Lance/) {
            diameter = 21  # Submarine-launched
        } else if (designation ~ /Ikara/) {
            diameter = 17.7  # Large ASW missile
        } else if (designation ~ /Stingray|Sea Urchin|Sea Spear/) {
            diameter = 12.75  # Modern lightweight
        } else {
            diameter = 12.75  # Default ASW
        }
    } else if (missile_type == "CIWS") {
        if (designation ~ /RAM/) {
            diameter = 5
        } else if (designation ~ /Sea Sparrow/) {
            diameter = 8
        } else {
            diameter = 8
        }
    } else {
        diameter = 13.5  # Default
    }

    # LENGTH estimation (feet)
    if (missile_type == "SAM") {
        if (designation ~ /Talos/) {
            missile_length = 21.0  # Large SAM
        } else if (designation ~ /Terrier|Sea Slug/) {
            missile_length = 15.0
        } else if (designation ~ /Standard ER|ERAM|SM-2ER|RIM-67/) {
            missile_length = 21.5
        } else if (designation ~ /Standard MR|SM-1MR|SM-2MR|RIM-66/) {
            missile_length = 14.8
        } else if (designation ~ /SM-3/) {
            missile_length = 21.5 + (year - 2005) * 0.1
        } else if (designation ~ /SM-6/) {
            missile_length = 21.5
        } else if (designation ~ /Sea Dart/) {
            missile_length = 14.5
        } else if (designation ~ /Sea Viper|Aster/) {
            missile_length = (designation ~ /Aster 30/) ? 15.6 : 13.1
        } else if (designation ~ /Type 03/) {
            missile_length = 15.0 + (year - 2003) * 0.05
        } else if (designation ~ /Type 07/) {
            missile_length = 16.0 + (year - 2007) * 0.04
        } else if (designation ~ /Sea Sparrow|RIM-7/) {
            missile_length = 12.0
        } else if (designation ~ /ESSM/) {
            missile_length = 12.0
        } else if (designation ~ /Sea Wolf/) {
            missile_length = 6.3
        } else if (designation ~ /CAMM/) {
            missile_length = (designation ~ /CAMM-ER/) ? 14.1 : 10.3
        } else if (designation ~ /RAM/) {
            missile_length = 9.2
        } else if (designation ~ /IRIS-T/) {
            missile_length = 9.7
        } else if (designation ~ /Bloodhound/) {
            missile_length = 24.9
        } else {
            missile_length = 14.8
        }
    } else if (missile_type == "SSM" || missile_type == "Cruise") {
        if (designation ~ /Tomahawk/) {
            missile_length = 18.3 + (year - 1983) * 0.02
        } else if (designation ~ /Harpoon/) {
            missile_length = 12.5 + (year - 1977) * 0.015
        } else if (designation ~ /Exocet MM40/) {
            missile_length = 19.0
        } else if (designation ~ /Exocet MM38/) {
            missile_length = 17.1
        } else if (designation ~ /Regulus I[^I]/) {
            missile_length = 33.0
        } else if (designation ~ /Regulus II/) {
            missile_length = 57.5
        } else if (designation ~ /SSM-1|Type 88/) {
            missile_length = 16.4
        } else if (designation ~ /Type 90/) {
            missile_length = 16.9
        } else if (designation ~ /Type 12/) {
            missile_length = 18.0 + (year - 2012) * 0.05
        } else if (designation ~ /LRASM/) {
            missile_length = 14.1
        } else if (designation ~ /NSM/) {
            missile_length = 13.0
        } else if (designation ~ /Penguin/) {
            missile_length = 9.8
        } else if (designation ~ /Sea Skua/) {
            missile_length = 8.9
        } else if (designation ~ /Kormoran/) {
            missile_length = 14.6
        } else if (designation ~ /ASM-1/) {
            missile_length = 13.1
        } else if (designation ~ /ASM-2/) {
            missile_length = 13.1
        } else if (designation ~ /ASM-3/) {
            missile_length = 19.7
        } else if (designation ~ /Storm Shadow/) {
            missile_length = 16.8
        } else if (designation ~ /JASSM/) {
            missile_length = (designation ~ /JASSM-ER/) ? 14.0 : 14.0
        } else if (designation ~ /JSOW/) {
            missile_length = 13.3
        } else if (designation ~ /CALCM|ACM/) {
            missile_length = 20.8
        } else if (designation ~ /Martlet|Sea Venom Light/) {
            missile_length = 5.2
        } else if (designation ~ /Sea Venom ANL/) {
            missile_length = 8.5
        } else if (designation ~ /CPS|Hypersonic/) {
            missile_length = 28.0
        } else {
            missile_length = 15.0
        }
    } else if (missile_type == "ASW") {
        if (designation ~ /ASROC|RUR-5/) {
            missile_length = 14.8
        } else if (designation ~ /VL-ASROC|VLA|Type 07 VLA/) {
            missile_length = 16.0 + (year - 1993) * 0.02
        } else if (designation ~ /SUBROC/) {
            missile_length = 20.5
        } else if (designation ~ /Sea Lance/) {
            missile_length = 20.0
        } else if (designation ~ /Ikara/) {
            missile_length = 11.3
        } else if (designation ~ /Weapon Alpha|Mk 108/) {
            missile_length = 7.2
        } else {
            missile_length = 14.8
        }
    } else if (missile_type == "CIWS") {
        if (designation ~ /RAM/) {
            missile_length = 9.2
        } else {
            missile_length = 12.0
        }
    } else {
        missile_length = 14.8
    }

    # WEIGHT estimation (lbs)
    weight = int(diameter * diameter * missile_length * 3.5)
    if (weight < 100) weight = 100
    if (weight > 8000) weight = 8000

    # WARHEAD estimation (lbs)
    if (missile_type == "SAM") {
        if (designation ~ /Nuclear/) {
            warhead = 1  # Nuclear warhead (kT not lbs)
        } else if (designation ~ /Talos|Sea Slug/) {
            warhead = 300 + (year - 1956) * 2
        } else if (designation ~ /Standard ER|ERAM|SM-2ER/) {
            warhead = 137 + (year - 1974) * 1.5
        } else if (designation ~ /Standard MR|SM-1MR|SM-2MR/) {
            warhead = 137
        } else if (designation ~ /SM-3/) {
            warhead = 0  # Kinetic kill
        } else if (designation ~ /SM-6/) {
            warhead = 140
        } else if (designation ~ /Sea Dart/) {
            warhead = 65
        } else if (designation ~ /Sea Viper|Aster/) {
            warhead = 33
        } else if (designation ~ /Type 03|Type 07/) {
            warhead = 150
        } else if (designation ~ /Sea Sparrow|ESSM/) {
            warhead = 86
        } else if (designation ~ /Sea Wolf|CAMM/) {
            warhead = 33
        } else if (designation ~ /RAM/) {
            warhead = 25
        } else if (designation ~ /IRIS-T/) {
            warhead = 25
        } else {
            warhead = 137
        }
    } else if (missile_type == "SSM" || missile_type == "Cruise") {
        if (designation ~ /Tomahawk/) {
            warhead = 1000
        } else if (designation ~ /Harpoon/) {
            warhead = 488
        } else if (designation ~ /Exocet/) {
            warhead = 364
        } else if (designation ~ /Regulus.*Nuclear/) {
            warhead = 1  # Nuclear
        } else if (designation ~ /Regulus/) {
            warhead = 3000
        } else if (designation ~ /SSM-1|Type 88|Type 90/) {
            warhead = 330
        } else if (designation ~ /Type 12/) {
            warhead = 440
        } else if (designation ~ /LRASM/) {
            warhead = 1000
        } else if (designation ~ /NSM/) {
            warhead = 276
        } else if (designation ~ /Penguin/) {
            warhead = 265
        } else if (designation ~ /Sea Skua/) {
            warhead = 66
        } else if (designation ~ /Kormoran/) {
            warhead = 363
        } else if (designation ~ /ASM-1/) {
            warhead = 330
        } else if (designation ~ /ASM-2/) {
            warhead = 330
        } else if (designation ~ /ASM-3/) {
            warhead = 400
        } else if (designation ~ /Storm Shadow/) {
            warhead = 880
        } else if (designation ~ /JASSM/) {
            warhead = 1000
        } else if (designation ~ /JSOW/) {
            warhead = 500
        } else if (designation ~ /CALCM/) {
            warhead = 3000
        } else if (designation ~ /ACM/) {
            warhead = 1  # Nuclear
        } else if (designation ~ /Martlet/) {
            warhead = 6.6
        } else if (designation ~ /Sea Venom/) {
            warhead = 66
        } else if (designation ~ /CPS|Hypersonic/) {
            warhead = 2000
        } else {
            warhead = 500
        }
    } else if (missile_type == "ASW") {
        if (designation ~ /Nuclear|SUBROC/) {
            warhead = 1  # Nuclear depth charge
        } else {
            warhead = 96  # Mk 46/54 torpedo warhead
        }
    } else if (missile_type == "CIWS") {
        warhead = 25
    } else {
        warhead = 200
    }

    # SPEED estimation (Mach)
    if (missile_type == "SAM") {
        if (designation ~ /Talos|Bloodhound/) {
            speed = 2.5
        } else if (designation ~ /Terrier|Standard ER|ERAM/) {
            speed = 2.5 + (year - 1967) * 0.01
        } else if (designation ~ /Standard MR|SM-1|SM-2MR/) {
            speed = 2.5
        } else if (designation ~ /SM-3/) {
            speed = 8.0 + (year - 2005) * 0.1
        } else if (designation ~ /SM-6/) {
            speed = 3.5
        } else if (designation ~ /Sea Dart/) {
            speed = 3.0
        } else if (designation ~ /Sea Viper|Aster/) {
            speed = 4.5
        } else if (designation ~ /Type 03|Type 07/) {
            speed = 3.0 + (year - 2003) * 0.02
        } else if (designation ~ /Sea Sparrow|ESSM/) {
            speed = 4.0
        } else if (designation ~ /Sea Wolf|CAMM/) {
            speed = 2.5 + (year - 1979) * 0.02
        } else if (designation ~ /RAM/) {
            speed = 2.0
        } else if (designation ~ /IRIS-T/) {
            speed = 3.0
        } else {
            speed = 2.5
        }
    } else if (missile_type == "SSM") {
        if (designation ~ /ASM-3/) {
            speed = 3.0  # Ramjet supersonic
        } else if (designation ~ /Tomahawk|Storm Shadow|JASSM|CALCM|Regulus/) {
            speed = 0.7  # Subsonic cruise
        } else if (designation ~ /Harpoon|Exocet|SSM-1|Type 88|Type 90/) {
            speed = 0.85  # High subsonic
        } else if (designation ~ /Type 12/) {
            speed = 0.9 + (year - 2012) * 0.01
        } else if (designation ~ /LRASM/) {
            speed = 0.85
        } else if (designation ~ /NSM/) {
            speed = 0.95
        } else if (designation ~ /Penguin|Sea Skua|Kormoran|Martlet|Sea Venom/) {
            speed = 0.8
        } else if (designation ~ /CPS|Hypersonic/) {
            speed = 10.0
        } else {
            speed = 0.85
        }
    } else if (missile_type == "Cruise") {
        speed = 0.7
    } else if (missile_type == "ASW") {
        speed = 1.0  # Rocket motor
    } else if (missile_type == "CIWS") {
        speed = 2.0
    } else {
        speed = 2.0
    }

    # RANGE estimation (nautical miles)
    if (missile_type == "SAM") {
        if (designation ~ /Talos/) {
            range_nm = 65 + (year - 1959) * 1.0
        } else if (designation ~ /Standard ER|ERAM|SM-2ER|RIM-67/) {
            range_nm = 90 + (year - 1974) * 1.5
        } else if (designation ~ /Standard MR|SM-1MR|SM-2MR|RIM-66/) {
            range_nm = 40 + (year - 1971) * 0.8
        } else if (designation ~ /SM-3/) {
            range_nm = 300 + (year - 2005) * 10
        } else if (designation ~ /SM-6/) {
            range_nm = 130 + (year - 2013) * 5
        } else if (designation ~ /Sea Dart/) {
            range_nm = 30 + (year - 1973) * 1.2
        } else if (designation ~ /Sea Slug/) {
            range_nm = 18 + (year - 1961) * 0.5
        } else if (designation ~ /Sea Viper|Aster 30/) {
            range_nm = 60
        } else if (designation ~ /Aster 15/) {
            range_nm = 16
        } else if (designation ~ /Type 03/) {
            range_nm = 27 + (year - 2003) * 1.0
        } else if (designation ~ /Type 07/) {
            range_nm = 32 + (year - 2007) * 1.5
        } else if (designation ~ /Sea Sparrow|RIM-7/) {
            range_nm = 8 + (year - 1969) * 0.3
        } else if (designation ~ /ESSM/) {
            range_nm = 27
        } else if (designation ~ /Sea Wolf/) {
            range_nm = 3.2 + (year - 1979) * 0.15
        } else if (designation ~ /CAMM-ER/) {
            range_nm = 30
        } else if (designation ~ /CAMM/) {
            range_nm = 13.5
        } else if (designation ~ /RAM/) {
            range_nm = 5.4 + (year - 1992) * 0.2
        } else if (designation ~ /IRIS-T/) {
            range_nm = 22
        } else if (designation ~ /Bloodhound/) {
            range_nm = 45
        } else {
            range_nm = 40
        }
    } else if (missile_type == "SSM") {
        if (designation ~ /Tomahawk/) {
            range_nm = 675 + (year - 1983) * 25
            if (range_nm > 1550) range_nm = 1550
        } else if (designation ~ /Harpoon Block II\+|RGM-84L/) {
            range_nm = 150
        } else if (designation ~ /Harpoon Block II/) {
            range_nm = 75
        } else if (designation ~ /Harpoon/) {
            range_nm = 60
        } else if (designation ~ /Exocet MM40 Block 3/) {
            range_nm = 100
        } else if (designation ~ /Exocet MM40/) {
            range_nm = 43
        } else if (designation ~ /Exocet MM38/) {
            range_nm = 23
        } else if (designation ~ /Regulus/) {
            range_nm = 500
        } else if (designation ~ /SSM-1|Type 88/) {
            range_nm = 100
        } else if (designation ~ /Type 90/) {
            range_nm = 108
        } else if (designation ~ /Type 12 SSM Block 2/) {
            range_nm = 540
        } else if (designation ~ /Type 12 SSM Block 1/) {
            range_nm = 400
        } else if (designation ~ /Type 12 SSM/) {
            range_nm = 108
        } else if (designation ~ /LRASM/) {
            range_nm = 300
        } else if (designation ~ /NSM/) {
            range_nm = 100
        } else if (designation ~ /Penguin/) {
            range_nm = 21
        } else if (designation ~ /Sea Skua/) {
            range_nm = 8
        } else if (designation ~ /Kormoran/) {
            range_nm = 16
        } else if (designation ~ /ASM-1/) {
            range_nm = 27
        } else if (designation ~ /ASM-2/) {
            range_nm = 48
        } else if (designation ~ /ASM-3/) {
            range_nm = 81
        } else if (designation ~ /Storm Shadow/) {
            range_nm = 270
        } else if (designation ~ /JASSM-ER/) {
            range_nm = 540
        } else if (designation ~ /JASSM/) {
            range_nm = 200
        } else if (designation ~ /JSOW/) {
            range_nm = 70
        } else if (designation ~ /CALCM|ACM|GLCM|Gryphon/) {
            range_nm = 1500
        } else if (designation ~ /Martlet/) {
            range_nm = 4
        } else if (designation ~ /Sea Venom/) {
            range_nm = 11
        } else if (designation ~ /IDAS/) {
            range_nm = 11
        } else if (designation ~ /CPS|Hypersonic/) {
            range_nm = 1700
        } else {
            range_nm = 75
        }
    } else if (missile_type == "Cruise") {
        range_nm = 675 + (year - 1983) * 25
        if (range_nm > 1550) range_nm = 1550
    } else if (missile_type == "ASW") {
        if (designation ~ /ASROC|RUR-5/) {
            range_nm = 5.4 + (year - 1961) * 0.05
        } else if (designation ~ /VL-ASROC|VLA|Type 07 VLA/) {
            range_nm = 12 + (year - 1993) * 0.3
        } else if (designation ~ /SUBROC|Sea Lance/) {
            range_nm = 30
        } else if (designation ~ /Ikara/) {
            range_nm = 10.8 + (year - 1968) * 0.2
        } else if (designation ~ /Weapon Alpha|Mk 108|Mk 112|Mk 113/) {
            range_nm = 0.4
        } else {
            range_nm = 10
        }
    } else if (missile_type == "CIWS") {
        range_nm = 5
    } else {
        range_nm = 50
    }

    # GUIDANCE system
    if (missile_type == "SAM") {
        if (designation ~ /Talos.*Beam|Tartar.*Beam/) {
            guidance = "Beam-riding"
        } else if (designation ~ /Terrier|Standard|SM-1|SM-2|Sea Dart|Type 03|Type 07|Aster/) {
            guidance = "Semi-active radar homing"
        } else if (designation ~ /SM-3/) {
            guidance = "Inertial + kinetic kill vehicle"
        } else if (designation ~ /SM-6|ERAM/) {
            guidance = "Active radar homing + semi-active"
        } else if (designation ~ /Sea Sparrow|ESSM/) {
            guidance = "Semi-active radar homing"
        } else if (designation ~ /Sea Wolf|CAMM/) {
            guidance = "Active radar homing"
        } else if (designation ~ /RAM/) {
            guidance = "Passive RF + infrared homing"
        } else if (designation ~ /IRIS-T|Type 91|Type 93/) {
            guidance = "Infrared imaging homing"
        } else if (designation ~ /Bloodhound/) {
            guidance = "Semi-active radar homing"
        } else if (designation ~ /ARM|Anti-Radiation/) {
            guidance = "Passive radar homing (anti-radiation)"
        } else {
            guidance = "Semi-active radar homing"
        }
    } else if (missile_type == "SSM") {
        if (designation ~ /Tomahawk|Storm Shadow|JASSM|CALCM/) {
            guidance = "INS + GPS + TERCOM + DSMAC"
        } else if (designation ~ /Regulus/) {
            guidance = "Radio command guidance"
        } else if (designation ~ /Harpoon|Exocet/) {
            guidance = "Active radar homing + inertial"
        } else if (designation ~ /SSM-1|Type 88|Type 90|Type 12/) {
            guidance = "Active radar homing + inertial"
        } else if (designation ~ /LRASM/) {
            guidance = "Passive RF + active radar + infrared + data-link"
        } else if (designation ~ /NSM/) {
            guidance = "Inertial + GPS + imaging infrared + data-link"
        } else if (designation ~ /Penguin|Sea Skua/) {
            guidance = "Infrared homing"
        } else if (designation ~ /Kormoran/) {
            guidance = "Inertial + active radar homing"
        } else if (designation ~ /ASM-1|ASM-2/) {
            guidance = "Active radar homing + inertial"
        } else if (designation ~ /ASM-3/) {
            guidance = "Inertial + active radar homing + ramjet"
        } else if (designation ~ /JSOW/) {
            guidance = "INS + GPS + imaging infrared"
        } else if (designation ~ /ACM/) {
            guidance = "INS + TERCOM + radar altimeter"
        } else if (designation ~ /Martlet|Sea Venom/) {
            guidance = "Semi-active laser homing"
        } else if (designation ~ /IDAS/) {
            guidance = "Fiber-optic guidance"
        } else if (designation ~ /CPS|Hypersonic/) {
            guidance = "INS + GPS + terminal maneuvering"
        } else {
            guidance = "Active radar homing"
        }
    } else if (missile_type == "Cruise") {
        guidance = "INS + GPS + TERCOM"
    } else if (missile_type == "ASW") {
        if (designation ~ /Nuclear|SUBROC/) {
            guidance = "Inertial + nuclear depth charge"
        } else {
            guidance = "Inertial + acoustic homing torpedo"
        }
    } else if (missile_type == "CIWS") {
        if (designation ~ /RAM/) {
            guidance = "Passive RF + infrared homing"
        } else {
            guidance = "Semi-active radar homing"
        }
    } else {
        guidance = "Active radar homing"
    }

    # PROPULSION type
    if (missile_type == "SAM") {
        if (designation ~ /SM-3/) {
            propulsion = "Three-stage solid fuel + KKV thrusters"
        } else if (designation ~ /Talos|Terrier|Standard|Sea Dart|Type 03|Type 07|Aster|ESSM|CAMM|RAM|IRIS-T/) {
            propulsion = "Solid-fuel rocket motor"
        } else if (designation ~ /Sea Sparrow/) {
            propulsion = "Solid-fuel rocket motor"
        } else if (designation ~ /Sea Wolf/) {
            propulsion = "Solid-fuel boost + sustain motor"
        } else if (designation ~ /Bloodhound/) {
            propulsion = "Ramjet + boosters"
        } else {
            propulsion = "Solid-fuel rocket motor"
        }
    } else if (missile_type == "SSM") {
        if (designation ~ /Tomahawk|Storm Shadow|JASSM|CALCM|Regulus|ACM|Gryphon/) {
            propulsion = "Turbofan jet engine + booster"
        } else if (designation ~ /Harpoon|Exocet|SSM-1|Type 88|Type 90/) {
            propulsion = "Turbojet + solid-fuel booster"
        } else if (designation ~ /Type 12/) {
            propulsion = "Turbojet + solid-fuel booster"
        } else if (designation ~ /LRASM/) {
            propulsion = "Turbofan jet engine"
        } else if (designation ~ /NSM/) {
            propulsion = "Turbojet + solid-fuel booster"
        } else if (designation ~ /Penguin|Sea Skua|Kormoran|Martlet|Sea Venom/) {
            propulsion = "Solid-fuel rocket motor"
        } else if (designation ~ /ASM-1|ASM-2/) {
            propulsion = "Turbojet + solid-fuel booster"
        } else if (designation ~ /ASM-3/) {
            propulsion = "Integral rocket ramjet + booster"
        } else if (designation ~ /JSOW/) {
            propulsion = "Unpowered glide"
        } else if (designation ~ /IDAS/) {
            propulsion = "Solid-fuel rocket motor"
        } else if (designation ~ /CPS|Hypersonic/) {
            propulsion = "Three-stage solid-fuel + HGV"
        } else {
            propulsion = "Turbojet + booster"
        }
    } else if (missile_type == "Cruise") {
        propulsion = "Turbofan jet engine + booster"
    } else if (missile_type == "ASW") {
        if (designation ~ /Weapon Alpha|Mk 108|Mk 112|Mk 113/) {
            propulsion = "Solid-fuel rocket motor"
        } else {
            propulsion = "Solid-fuel rocket motor + torpedo payload"
        }
    } else if (missile_type == "CIWS") {
        propulsion = "Solid-fuel rocket motor"
    } else {
        propulsion = "Solid-fuel rocket motor"
    }

    # TARGET types
    if (missile_type == "SAM") {
        targets = "Aircraft, cruise missiles, ballistic missiles"
    } else if (missile_type == "SSM" || missile_type == "Cruise") {
        if (designation ~ /Tomahawk|Storm Shadow|JASSM|CALCM|ACM|Gryphon/) {
            targets = "Land targets, surface ships"
        } else {
            targets = "Surface ships"
        }
    } else if (missile_type == "ASW") {
        targets = "Submarines"
    } else if (missile_type == "CIWS") {
        targets = "Anti-ship missiles, aircraft"
    } else {
        targets = "Various"
    }

    # PLATFORM types
    if (missile_type == "SAM" || missile_type == "CIWS") {
        platform = "Surface ships, VLS"
    } else if (missile_type == "SSM") {
        if (designation ~ /Tomahawk|Storm Shadow|JASSM|CALCM|ACM/) {
            platform = "Surface ships, submarines, VLS"
        } else if (designation ~ /Penguin|Sea Skua|Sea Venom|Martlet/) {
            platform = "Helicopters, patrol boats"
        } else if (designation ~ /IDAS/) {
            platform = "Submarines"
        } else if (designation ~ /ASM-/) {
            platform = "Aircraft, helicopters"
        } else {
            platform = "Surface ships, VLS"
        }
    } else if (missile_type == "Cruise") {
        platform = "Surface ships, submarines, VLS"
    } else if (missile_type == "ASW") {
        if (designation ~ /SUBROC|Sea Lance/) {
            platform = "Submarines"
        } else {
            platform = "Surface ships, VLS"
        }
    } else {
        platform = "Surface ships"
    }

    # Format output for naval_missiles_database.md schema
    # Schema: Missile_ID | Country | Designation | Type | Year | Diameter | Length | Weight | Warhead_Weight | Speed | Range | Guidance | Propulsion | Targets | Platform | Is_Starting_Tech | Modded
    printf "| %s | %s | %s | %s | %s | %.1f | %.1f | %d | %s | %.2f | %.1f | %s | %s | %s | %s | %d | 0 |\n", \
        missile_id, country, designation, missile_type, year, \
        diameter, missile_length, weight, \
        (warhead == 1) ? "Nuclear" : warhead, \
        speed, range_nm, \
        guidance, propulsion, targets, platform, \
        (research_cost == 0) ? 1 : 0
}
