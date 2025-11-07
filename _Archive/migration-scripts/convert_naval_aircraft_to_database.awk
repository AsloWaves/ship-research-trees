BEGIN {
    FS = "|"
    OFS = "|"
    print "# Converting naval aircraft research nodes to detailed database entries"
    print "# Estimating specifications based on type, year, and designation"
}

/^\| [0-9]/ {
    # Extract fields
    gsub(/^[ \t]+|[ \t]+$/, "", $2)  # Node_ID
    gsub(/^[ \t]+|[ \t]+$/, "", $3)  # Nation
    gsub(/^[ \t]+|[ \t]+$/, "", $4)  # Designation
    gsub(/^[ \t]+|[ \t]+$/, "", $5)  # Year
    gsub(/^[ \t]+|[ \t]+$/, "", $6)  # Tech_Branch
    gsub(/^[ \t]+|[ \t]+$/, "", $7)  # Type

    aircraft_id = $2
    country = $3
    designation = $4
    year = $5
    tech_branch = $6
    aircraft_type = $7

    # Skip if not naval aircraft
    if (tech_branch != "Naval Aircraft") next

    # Initialize variables
    wingspan = 0
    length_ft = 0
    max_weight = 0
    empty_weight = 0
    max_speed_kts = 0
    combat_radius = 0
    service_ceiling = 0
    engine_type = ""
    engine_count = 0
    crew = 0
    armament = 0
    role = ""

    # WINGSPAN estimation (feet)
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        # WWII prop fighters
        if (designation ~ /Wildcat|F4F/) {
            wingspan = 38
        } else if (designation ~ /Hellcat|F6F/) {
            wingspan = 42.8
        } else if (designation ~ /Bearcat|F8F/) {
            wingspan = 35.5
        } else if (designation ~ /Hurricane/) {
            wingspan = 40
        } else if (designation ~ /Seafire/) {
            wingspan = 36.8
        } else if (designation ~ /Sea Fury/) {
            wingspan = 38.4
        } else if (designation ~ /Zero|A6M/) {
            wingspan = 39.4
        } else if (designation ~ /Raiden|J2M/) {
            wingspan = 35.4
        } else if (designation ~ /Shiden|N1K/) {
            wingspan = 39.4
        } else {
            wingspan = 38
        }
    } else if (aircraft_type ~ /Jet Fighter|Multi-Role|Interceptor/) {
        if (designation ~ /Panther|F9F-[0-5]/) {
            wingspan = 38
        } else if (designation ~ /Cougar|F9F-8/) {
            wingspan = 34.5
        } else if (designation ~ /Tiger|F11F/) {
            wingspan = 31.6
        } else if (designation ~ /Crusader|F8U/) {
            wingspan = 35.6
        } else if (designation ~ /Phantom|F-4/) {
            wingspan = 38.4
        } else if (designation ~ /Tomcat|F-14/) {
            wingspan = 64  # Variable sweep, max
        } else if (designation ~ /Hornet|F\/A-18[A-D]/) {
            wingspan = 40.4
        } else if (designation ~ /Super Hornet|F\/A-18[EF]/) {
            wingspan = 44.8
        } else if (designation ~ /Lightning II|F-35/) {
            wingspan = 35
        } else if (designation ~ /Attacker/) {
            wingspan = 36.9
        } else if (designation ~ /Sea Hawk/) {
            wingspan = 39
        } else if (designation ~ /Sea Venom/) {
            wingspan = 42.8
        } else if (designation ~ /Scimitar/) {
            wingspan = 37.1
        } else if (designation ~ /Sea Vixen/) {
            wingspan = 50
        } else if (designation ~ /Harrier|Sea Harrier/) {
            wingspan = 25.25
        } else if (designation ~ /Tornado/) {
            wingspan = 45.6  # Swept
        } else if (designation ~ /Typhoon|Eurofighter/) {
            wingspan = 35.9
        } else {
            wingspan = 40
        }
    } else if (aircraft_type ~ /Dive Bomber|Torpedo Bomber|Strike|Attack/) {
        if (designation ~ /Dauntless|SBD/) {
            wingspan = 41.5
        } else if (designation ~ /Helldiver|SB2C/) {
            wingspan = 49.8
        } else if (designation ~ /Skyraider|AD/) {
            wingspan = 50
        } else if (designation ~ /Skyhawk|A-4/) {
            wingspan = 27.5
        } else if (designation ~ /Intruder|A-6/) {
            wingspan = 53
        } else if (designation ~ /Corsair II|A-7/) {
            wingspan = 38.7
        } else if (designation ~ /Avenger|TBF|TBM/) {
            wingspan = 54.1
        } else if (designation ~ /Swordfish/) {
            wingspan = 45.5
        } else if (designation ~ /Barracuda/) {
            wingspan = 49.1
        } else if (designation ~ /Firefly/) {
            wingspan = 41.1
        } else if (designation ~ /Wyvern/) {
            wingspan = 44
        } else if (designation ~ /Buccaneer/) {
            wingspan = 44
        } else if (designation ~ /Val|D3A/) {
            wingspan = 47.5
        } else if (designation ~ /Judy|D4Y/) {
            wingspan = 37.8
        } else if (designation ~ /Grace|B7A/) {
            wingspan = 47.3
        } else if (designation ~ /Kate|B5N/) {
            wingspan = 50.9
        } else if (designation ~ /Jill|B6N/) {
            wingspan = 48.8
        } else {
            wingspan = 45
        }
    } else if (aircraft_type ~ /ASW/) {
        if (designation ~ /Tracker|S-2/) {
            wingspan = 69.6
        } else if (designation ~ /Viking|S-3/) {
            wingspan = 68.6
        } else if (designation ~ /Orion|P-3/) {
            wingspan = 99.6
        } else if (designation ~ /Poseidon|P-8/) {
            wingspan = 123.5
        } else if (designation ~ /Gannet/) {
            wingspan = 54.3
        } else if (designation ~ /Nimrod/) {
            wingspan = 114.8
        } else if (designation ~ /Atlantic/) {
            wingspan = 119.1
        } else if (designation ~ /Neptune|P2V/) {
            wingspan = 103.3
        } else if (designation ~ /PS-1|US-2/) {
            wingspan = 108.8
        } else if (designation ~ /P-1/) {
            wingspan = 114.8
        } else {
            wingspan = 90
        }
    } else if (aircraft_type ~ /AEW|EW|Recon/) {
        if (designation ~ /Tracer|E-1/) {
            wingspan = 69.6
        } else if (designation ~ /Hawkeye|E-2/) {
            wingspan = 80.6
        } else if (designation ~ /Prowler|EA-6/) {
            wingspan = 53
        } else if (designation ~ /Growler|EA-18/) {
            wingspan = 44.8
        } else if (designation ~ /Vigilante|RA-5/) {
            wingspan = 53
        } else {
            wingspan = 60
        }
    } else if (aircraft_type ~ /Helo|Helicopter/) {
        if (designation ~ /Sea King|SH-3|HSS/) {
            wingspan = 62  # Rotor diameter
        } else if (designation ~ /Seahawk|SH-60|MH-60/) {
            wingspan = 53.7
        } else if (designation ~ /Wasp/) {
            wingspan = 32.3
        } else if (designation ~ /Lynx/) {
            wingspan = 42
        } else if (designation ~ /Wildcat/) {
            wingspan = 42.6
        } else if (designation ~ /Merlin|MCH-101/) {
            wingspan = 61
        } else if (designation ~ /NH90|Sea Lion/) {
            wingspan = 53.1
        } else if (designation ~ /OH-6|OH-1/) {
            wingspan = 26.4
        } else {
            wingspan = 50
        }
    } else if (aircraft_type ~ /UAV/) {
        wingspan = 75  # MQ-25
    } else {
        wingspan = 40
    }

    # LENGTH estimation (feet)
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        length_ft = wingspan * 0.75  # Typical prop fighter ratio
    } else if (aircraft_type ~ /Jet Fighter|Multi-Role|Interceptor/) {
        if (designation ~ /Tomcat|F-14/) {
            length_ft = 62.8
        } else if (designation ~ /Phantom|F-4/) {
            length_ft = 63
        } else if (designation ~ /Super Hornet|F\/A-18[EF]/) {
            length_ft = 60.2
        } else if (designation ~ /Hornet|F\/A-18/) {
            length_ft = 56
        } else if (designation ~ /Lightning II|F-35/) {
            length_ft = 51.4
        } else if (designation ~ /Harrier/) {
            length_ft = 46.3
        } else if (designation ~ /Typhoon/) {
            length_ft = 52.3
        } else {
            length_ft = wingspan * 1.1
        }
    } else if (aircraft_type ~ /Attack|Strike/) {
        if (designation ~ /Intruder|A-6/) {
            length_ft = 54.8
        } else if (designation ~ /Skyraider|AD/) {
            length_ft = 38.8
        } else if (designation ~ /Skyhawk|A-4/) {
            length_ft = 42.2
        } else if (designation ~ /Buccaneer/) {
            length_ft = 63.4
        } else {
            length_ft = wingspan * 0.95
        }
    } else if (aircraft_type ~ /ASW/) {
        if (designation ~ /Poseidon|P-8/) {
            length_ft = 129.5
        } else if (designation ~ /Orion|P-3/) {
            length_ft = 116.8
        } else if (designation ~ /Viking|S-3/) {
            length_ft = 53.3
        } else if (designation ~ /Nimrod/) {
            length_ft = 126.8
        } else if (designation ~ /P-1/) {
            length_ft = 124.6
        } else {
            length_ft = wingspan * 1.15
        }
    } else if (aircraft_type ~ /Helo/) {
        length_ft = wingspan * 0.85
    } else {
        length_ft = wingspan * 1.0
    }

    # MAX WEIGHT estimation (lbs)
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        max_weight = 8000 + (year - 1940) * 100
        if (max_weight > 13500) max_weight = 13500
    } else if (aircraft_type ~ /Stealth/) {
        max_weight = 70000
    } else if (aircraft_type ~ /Interceptor|Multi-Role/) {
        if (designation ~ /Tomcat/) {
            max_weight = 74350
        } else if (designation ~ /Phantom/) {
            max_weight = 61650
        } else if (designation ~ /Super Hornet/) {
            max_weight = 66000
        } else {
            max_weight = 25000 + (year - 1950) * 500
            if (max_weight > 75000) max_weight = 75000
        }
    } else if (aircraft_type ~ /Attack|Strike/) {
        max_weight = 18000 + (year - 1945) * 400
        if (max_weight > 60000) max_weight = 60000
    } else if (aircraft_type ~ /ASW/) {
        if (designation ~ /Poseidon|P-8/) {
            max_weight = 189200
        } else if (designation ~ /Orion|P-3/) {
            max_weight = 142000
        } else {
            max_weight = 50000 + (year - 1955) * 1000
            if (max_weight > 190000) max_weight = 190000
        }
    } else if (aircraft_type ~ /Helo/) {
        max_weight = 12000 + (year - 1960) * 150
        if (max_weight > 23500) max_weight = 23500
    } else if (aircraft_type ~ /UAV/) {
        max_weight = 51000
    } else {
        max_weight = 30000
    }

    # EMPTY WEIGHT (60-65% of max weight)
    empty_weight = int(max_weight * 0.62)

    # MAX SPEED estimation (knots)
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        max_speed_kts = 290 + (year - 1940) * 8
        if (max_speed_kts > 410) max_speed_kts = 410
    } else if (aircraft_type ~ /Stealth/) {
        max_speed_kts = designation ~ /F-35/ ? 1200 : 1000
    } else if (aircraft_type ~ /Jet Fighter|Interceptor|Multi-Role/) {
        if (designation ~ /Tomcat|F-14/) {
            max_speed_kts = 1240
        } else if (designation ~ /Phantom|F-4/) {
            max_speed_kts = 1470
        } else if (designation ~ /Super Hornet/) {
            max_speed_kts = 1190
        } else if (designation ~ /Harrier/) {
            max_speed_kts = 650
        } else {
            max_speed_kts = 600 + (year - 1949) * 12
            if (max_speed_kts > 1500) max_speed_kts = 1500
        }
    } else if (aircraft_type ~ /Attack|Strike/) {
        max_speed_kts = 350 + (year - 1945) * 8
        if (max_speed_kts > 650) max_speed_kts = 650
    } else if (aircraft_type ~ /ASW/) {
        max_speed_kts = 250 + (year - 1950) * 5
        if (max_speed_kts > 490) max_speed_kts = 490
    } else if (aircraft_type ~ /Helo/) {
        max_speed_kts = 120 + (year - 1960) * 1.5
        if (max_speed_kts > 180) max_speed_kts = 180
    } else if (aircraft_type ~ /UAV/) {
        max_speed_kts = 350
    } else {
        max_speed_kts = 500
    }

    # COMBAT RADIUS estimation (nautical miles)
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        combat_radius = 250 + (year - 1940) * 15
    } else if (aircraft_type ~ /Stealth/) {
        combat_radius = 550
    } else if (aircraft_type ~ /Jet Fighter|Interceptor/) {
        combat_radius = 400 + (year - 1950) * 5
        if (combat_radius > 750) combat_radius = 750
    } else if (aircraft_type ~ /Multi-Role/) {
        combat_radius = 450 + (year - 1960) * 8
        if (combat_radius > 850) combat_radius = 850
    } else if (aircraft_type ~ /Attack|Strike/) {
        combat_radius = 600 + (year - 1945) * 10
        if (combat_radius > 1200) combat_radius = 1200
    } else if (aircraft_type ~ /ASW/) {
        if (designation ~ /Poseidon|P-8/) {
            combat_radius = 1200
        } else if (designation ~ /Orion|P-3/) {
            combat_radius = 1200
        } else {
            combat_radius = 800 + (year - 1955) * 10
            if (combat_radius > 1500) combat_radius = 1500
        }
    } else if (aircraft_type ~ /Helo/) {
        combat_radius = 150 + (year - 1960) * 5
        if (combat_radius > 350) combat_radius = 350
    } else if (aircraft_type ~ /UAV/) {
        combat_radius = 500
    } else {
        combat_radius = 500
    }

    # SERVICE CEILING estimation (feet)
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        service_ceiling = 30000 + (year - 1940) * 500
        if (service_ceiling > 39000) service_ceiling = 39000
    } else if (aircraft_type ~ /Stealth/) {
        service_ceiling = 50000
    } else if (aircraft_type ~ /Jet Fighter|Interceptor|Multi-Role/) {
        service_ceiling = 45000 + (year - 1950) * 200
        if (service_ceiling > 65000) service_ceiling = 65000
    } else if (aircraft_type ~ /Attack|Strike/) {
        service_ceiling = 35000 + (year - 1945) * 150
        if (service_ceiling > 50000) service_ceiling = 50000
    } else if (aircraft_type ~ /ASW/) {
        service_ceiling = 25000 + (year - 1950) * 200
        if (service_ceiling > 42000) service_ceiling = 42000
    } else if (aircraft_type ~ /Helo/) {
        service_ceiling = 10000 + (year - 1960) * 100
        if (service_ceiling > 20000) service_ceiling = 20000
    } else {
        service_ceiling = 40000
    }

    # ENGINE TYPE
    if (aircraft_type ~ /Jet|Multi-Role|Interceptor|Stealth/) {
        if (year >= 1970) {
            engine_type = "Turbofan"
        } else {
            engine_type = "Turbojet"
        }
    } else if (aircraft_type ~ /ASW/ && aircraft_type !~ /Helo/) {
        engine_type = "Turboprop"
    } else if (aircraft_type ~ /Helo/) {
        engine_type = "Turboshaft"
    } else if (aircraft_type ~ /UAV/) {
        engine_type = "Turbofan"
    } else {
        engine_type = "Piston radial"
    }

    # ENGINE COUNT
    if (aircraft_type ~ /Helo|UAV/) {
        engine_count = 1
    } else if (aircraft_type ~ /Fighter|Attack/ && aircraft_type !~ /Intruder|Prowler|Buccaneer|Phantom/) {
        engine_count = 1
    } else if (aircraft_type ~ /ASW/ && designation !~ /Tracker|Viking|Gannet/) {
        engine_count = 4
    } else {
        engine_count = 2
    }

    # CREW
    if (aircraft_type ~ /UAV/) {
        crew = 0
    } else if (aircraft_type ~ /Helo/) {
        crew = designation ~ /ASW|Multi-Role/ ? 3 : 2
    } else if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        crew = 1
    } else if (designation ~ /Phantom|Tomcat|Intruder|Prowler|Buccaneer|Viking|Sea Vixen/) {
        crew = 2
    } else if (aircraft_type ~ /ASW/ && aircraft_type !~ /Helo/) {
        crew = designation ~ /Tracker|Gannet/ ? 4 : 10
    } else if (aircraft_type ~ /AEW|EW/) {
        crew = 5
    } else {
        crew = 1
    }

    # ARMAMENT CAPACITY estimation (lbs)
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        armament = 2000
    } else if (aircraft_type ~ /Stealth/) {
        armament = 18000
    } else if (aircraft_type ~ /Interceptor/) {
        armament = 14500
    } else if (aircraft_type ~ /Multi-Role/) {
        armament = 17750
    } else if (aircraft_type ~ /Attack|Strike/) {
        armament = 15000 + (year - 1945) * 100
        if (armament > 28000) armament = 28000
    } else if (aircraft_type ~ /ASW/ && aircraft_type !~ /Helo/) {
        armament = 20000
    } else if (aircraft_type ~ /Helo/) {
        armament = 4000
    } else if (aircraft_type ~ /AEW|EW|Recon/) {
        armament = 0
    } else if (aircraft_type ~ /UAV/) {
        armament = 0  # Tanker
    } else {
        armament = 8000
    }

    # ROLE description
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        role = "Carrier fighter"
    } else if (aircraft_type ~ /Jet Fighter/) {
        role = "Carrier jet fighter"
    } else if (aircraft_type ~ /Interceptor/) {
        role = "Fleet air defense interceptor"
    } else if (aircraft_type ~ /Multi-Role/) {
        role = "Multi-role fighter/attack"
    } else if (aircraft_type ~ /Stealth/) {
        role = "5th generation stealth multi-role"
    } else if (aircraft_type ~ /V\/STOL/) {
        role = "V/STOL carrier operations"
    } else if (aircraft_type ~ /Dive Bomber/) {
        role = "Dive bomber"
    } else if (aircraft_type ~ /Torpedo Bomber/) {
        role = "Torpedo bomber"
    } else if (aircraft_type ~ /Strike|Attack/) {
        role = "Strike/attack aircraft"
    } else if (aircraft_type ~ /ASW/ && aircraft_type !~ /Helo/) {
        role = "Anti-submarine warfare patrol"
    } else if (aircraft_type ~ /ASW Helo/) {
        role = "ASW helicopter"
    } else if (aircraft_type ~ /Multi-Role Helo/) {
        role = "Multi-role helicopter"
    } else if (aircraft_type ~ /AEW/) {
        role = "Airborne early warning"
    } else if (aircraft_type ~ /EW/) {
        role = "Electronic warfare"
    } else if (aircraft_type ~ /Recon/) {
        role = "Reconnaissance"
    } else if (aircraft_type ~ /UAV/) {
        role = "Unmanned aerial refueling"
    } else if (aircraft_type ~ /Observation/) {
        role = "Observation helicopter"
    } else if (aircraft_type ~ /Utility/) {
        role = "Utility helicopter"
    } else if (aircraft_type ~ /SAR/) {
        role = "Search and rescue"
    } else {
        role = "Naval aviation"
    }

    # Format output for naval_aircraft_database.md schema
    printf "| %s | %s | %s | %s | %s | %.1f | %.1f | %d | %d | %d | %d | %d | %s | %d | %d | %d | %s | %d | 0 |\n", \
        aircraft_id, country, designation, year, aircraft_type, \
        wingspan, length_ft, max_weight, empty_weight, \
        max_speed_kts, combat_radius, service_ceiling, \
        engine_type, engine_count, crew, armament, role, \
        (research_cost == 0) ? 1 : 0
}
