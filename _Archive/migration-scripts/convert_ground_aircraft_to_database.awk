#!/usr/bin/awk -f
# Convert ground aircraft research tree entries to detailed database specifications
# Estimates missing specifications based on aircraft type, designation, and year

BEGIN {
    FS = "|"
    OFS = "|"

    # Print database header
    print "| Node_ID | Nation | Designation | Year | Type | Wingspan_ft | Length_ft | Max_Weight_lbs | Empty_Weight_lbs | Max_Speed_kts | Cruise_Speed_kts | Service_Ceiling_ft | Engine_Type | Num_Engines | Crew | Combat_Radius_nm | Role | Is_Modded | Modded |"
    print "|---------|--------|-------------|------|------|-------------|-----------|----------------|------------------|---------------|------------------|-------------------|-------------|-------------|------|------------------|------|-----------|--------|"
}

/^\|/ && NF >= 10 {
    # Strip whitespace
    for (i = 1; i <= NF; i++) {
        gsub(/^[ \t]+|[ \t]+$/, "", $i)
    }

    node_id = $2
    nation = $3
    designation = $4
    year = $5
    tech_branch = $6
    aircraft_type = $7
    modded = $17

    # Skip header rows
    if (node_id ~ /Node_ID/ || node_id == "") next

    # WINGSPAN estimation (feet)
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet|Stealth/) {
        # WWII fighters
        if (designation ~ /P-38|Lightning/) wingspan = 52
        else if (designation ~ /P-40|Warhawk/) wingspan = 37.3
        else if (designation ~ /P-47|Thunderbolt/) wingspan = 40.9
        else if (designation ~ /P-51|Mustang/) wingspan = 37.0
        else if (designation ~ /Spitfire/) wingspan = 36.1
        else if (designation ~ /Hurricane/) wingspan = 40.0
        else if (designation ~ /Bf 109|Me 109/) wingspan = 32.5
        else if (designation ~ /Fw 190/) wingspan = 34.5
        else if (designation ~ /Zero|A6M/) wingspan = 39.4
        else if (designation ~ /Ki-43|Oscar/) wingspan = 35.8
        else if (designation ~ /Ki-61|Tony/) wingspan = 39.4
        else if (designation ~ /Ki-84|Frank/) wingspan = 36.1
        else wingspan = 35 + (year - 1940) * 0.3
    } else if (aircraft_type ~ /Jet Fighter|Interceptor/ && aircraft_type !~ /Stealth/) {
        # Early jets
        if (designation ~ /Meteor/) wingspan = 37.2
        else if (designation ~ /F-80|Shooting Star/) wingspan = 38.9
        else if (designation ~ /F-84|Thunderjet/) wingspan = 36.5
        else if (designation ~ /F-86|Sabre|CL-13/) wingspan = 37.1
        else if (designation ~ /Hunter/) wingspan = 33.8
        else if (designation ~ /F-100|Super Sabre/) wingspan = 38.9
        else if (designation ~ /F-104|Starfighter/) wingspan = 21.9
        else if (designation ~ /Lightning F\./) wingspan = 34.8
        else if (designation ~ /F-4|Phantom/) wingspan = 38.5
        else if (designation ~ /F-105|Thunderchief/) wingspan = 34.9
        else if (designation ~ /MiG-21|Fishbed/) wingspan = 23.5
        else if (designation ~ /F-8|Crusader/) wingspan = 35.8
        else wingspan = 35 + (year - 1945) * 0.1
    } else if (aircraft_type ~ /Multi-Role|Strike/ && aircraft_type !~ /Stealth/) {
        # Multi-role fighters
        if (designation ~ /Tornado/) wingspan = 45.7
        else if (designation ~ /F-15|Eagle/) wingspan = 42.8
        else if (designation ~ /F-16|Fighting Falcon/) wingspan = 32.8
        else if (designation ~ /F\/A-18|Hornet/) wingspan = 40.4
        else if (designation ~ /Typhoon|Eurofighter/) wingspan = 35.9
        else if (designation ~ /Rafale/) wingspan = 35.4
        else if (designation ~ /F-2/) wingspan = 36.1
        else wingspan = 38 + (year - 1970) * 0.05
    } else if (aircraft_type ~ /Stealth/) {
        # Stealth fighters
        if (designation ~ /F-22|Raptor/) wingspan = 44.5
        else if (designation ~ /F-35|Lightning/) wingspan = 35.0
        else if (designation ~ /F-117|Nighthawk/) wingspan = 43.3
        else wingspan = 42
    } else if (aircraft_type ~ /Bomber|Strategic/) {
        # Bombers
        if (designation ~ /B-17|Flying Fortress/) wingspan = 103.9
        else if (designation ~ /B-24|Liberator/) wingspan = 110.0
        else if (designation ~ /B-29|Superfortress/) wingspan = 141.3
        else if (designation ~ /Lancaster/) wingspan = 102.0
        else if (designation ~ /Lincoln/) wingspan = 120.0
        else if (designation ~ /He 111/) wingspan = 74.0
        else if (designation ~ /Ju 87|Stuka/) wingspan = 45.3
        else if (designation ~ /Ju 88/) wingspan = 65.6
        else if (designation ~ /B-47|Stratojet/) wingspan = 116.0
        else if (designation ~ /B-52|Stratofortress/) wingspan = 185.0
        else if (designation ~ /B-58|Hustler/) wingspan = 56.8
        else if (designation ~ /Vulcan/) wingspan = 111.0
        else if (designation ~ /Canberra/) wingspan = 63.9
        else if (designation ~ /B-1|Lancer/) wingspan = 137.0
        else if (designation ~ /B-2|Spirit/) wingspan = 172.0
        else if (designation ~ /B-21|Raider/) wingspan = 165.0
        else wingspan = 100 + (year - 1940) * 1.2
    } else if (aircraft_type ~ /Attack/) {
        # Attack aircraft
        if (designation ~ /A-4|Skyhawk/) wingspan = 27.5
        else if (designation ~ /A-6|Intruder/) wingspan = 53.0
        else if (designation ~ /A-7|Corsair/) wingspan = 38.7
        else if (designation ~ /A-10|Thunderbolt/) wingspan = 57.5
        else if (designation ~ /Harrier/) wingspan = 25.3
        else wingspan = 40 + (year - 1960) * 0.2
    } else if (aircraft_type ~ /Transport/) {
        # Transport aircraft
        if (designation ~ /C-1/) wingspan = 100.4
        else if (designation ~ /C-2/) wingspan = 144.5
        else if (designation ~ /C-130|Hercules/) wingspan = 132.6
        else if (designation ~ /C-160|Transall/) wingspan = 131.2
        else if (designation ~ /C-17|Globemaster/) wingspan = 169.8
        else if (designation ~ /A400M|Atlas/) wingspan = 139.1
        else if (designation ~ /KC-135|Stratotanker/) wingspan = 130.8
        else if (designation ~ /KC-767/) wingspan = 156.1
        else wingspan = 120 + (year - 1960) * 0.8
    } else if (aircraft_type ~ /Helo|Helicopter/) {
        # Helicopters
        if (designation ~ /UH-1|Huey|Iroquois/) wingspan = 48.0
        else if (designation ~ /AH-1|Cobra/) wingspan = 48.0
        else if (designation ~ /CH-47|Chinook/) wingspan = 60.0
        else if (designation ~ /UH-60|Black Hawk/) wingspan = 53.7
        else if (designation ~ /AH-64|Apache/) wingspan = 48.2
        else if (designation ~ /CH-53/) wingspan = 72.3
        else if (designation ~ /Tiger|UHT/) wingspan = 43.0
        else if (designation ~ /NH90/) wingspan = 52.1
        else if (designation ~ /Puma/) wingspan = 49.2
        else if (designation ~ /Merlin/) wingspan = 60.9
        else wingspan = 50
    } else {
        wingspan = 40  # Default
    }

    # LENGTH estimation (feet) - typically 0.8-1.2x wingspan
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Stealth/) {
        aircraft_length = wingspan * 1.15
    } else if (aircraft_type ~ /Stealth/) {
        aircraft_length = wingspan * 1.45
    } else if (aircraft_type ~ /Bomber/) {
        aircraft_length = wingspan * 0.65
    } else if (aircraft_type ~ /Transport/) {
        aircraft_length = wingspan * 0.75
    } else if (aircraft_type ~ /Helo/) {
        aircraft_length = wingspan * 1.3
    } else {
        aircraft_length = wingspan * 1.1
    }

    # MAX WEIGHT estimation (pounds)
    if (aircraft_type ~ /Stealth Fighter/) {
        if (designation ~ /F-22/) max_weight = 83500
        else if (designation ~ /F-35A/) max_weight = 70000
        else if (designation ~ /F-35B/) max_weight = 60000
        else if (designation ~ /F-117/) max_weight = 52500
        else max_weight = 70000
    } else if (aircraft_type ~ /Interceptor|Multi-Role|Strike/) {
        if (designation ~ /F-4/) max_weight = 61800
        else if (designation ~ /F-15/) max_weight = 81000
        else if (designation ~ /F-16/) max_weight = 42300
        else if (designation ~ /F\/A-18/) max_weight = 51900
        else if (designation ~ /Tornado/) max_weight = 61700
        else if (designation ~ /Typhoon/) max_weight = 52000
        else if (designation ~ /F-2/) max_weight = 50000
        else max_weight = 40000 + (year - 1960) * 600
    } else if (aircraft_type ~ /Jet Fighter/ && aircraft_type !~ /Multi/) {
        if (designation ~ /F-86/) max_weight = 20357
        else if (designation ~ /F-100/) max_weight = 34832
        else if (designation ~ /F-104/) max_weight = 28779
        else if (designation ~ /Meteor/) max_weight = 20000
        else if (designation ~ /Hunter/) max_weight = 24000
        else if (designation ~ /Lightning/) max_weight = 50000
        else max_weight = 15000 + (year - 1945) * 400
    } else if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        # WWII fighters
        max_weight = 8000 + (year - 1940) * 500
    } else if (aircraft_type ~ /Strategic Bomber/) {
        if (designation ~ /B-52/) max_weight = 488000
        else if (designation ~ /B-1/) max_weight = 477000
        else if (designation ~ /B-2/) max_weight = 376000
        else if (designation ~ /B-21/) max_weight = 360000
        else if (designation ~ /Vulcan/) max_weight = 204000
        else max_weight = 200000 + (year - 1950) * 3000
    } else if (aircraft_type ~ /Bomber/ && aircraft_type !~ /Strategic/) {
        if (designation ~ /B-17/) max_weight = 65500
        else if (designation ~ /B-29/) max_weight = 141100
        else if (designation ~ /Lancaster/) max_weight = 72000
        else if (designation ~ /B-47/) max_weight = 230000
        else max_weight = 50000 + (year - 1940) * 2000
    } else if (aircraft_type ~ /Attack/) {
        if (designation ~ /A-10/) max_weight = 51000
        else if (designation ~ /A-6/) max_weight = 60400
        else max_weight = 30000 + (year - 1960) * 400
    } else if (aircraft_type ~ /Transport/) {
        if (designation ~ /C-130/) max_weight = 175000
        else if (designation ~ /C-17/) max_weight = 585000
        else if (designation ~ /A400M/) max_weight = 310000
        else if (designation ~ /C-160/) max_weight = 112400
        else max_weight = 100000 + (year - 1960) * 3000
    } else if (aircraft_type ~ /Helo/) {
        if (designation ~ /AH-64/) max_weight = 23000
        else if (designation ~ /UH-60/) max_weight = 23500
        else if (designation ~ /CH-47/) max_weight = 50000
        else if (designation ~ /CH-53/) max_weight = 73500
        else max_weight = 15000 + (year - 1960) * 200
    } else {
        max_weight = 25000  # Default
    }

    # EMPTY WEIGHT (typically 55-65% of max weight)
    empty_weight = int(max_weight * 0.60)

    # MAX SPEED estimation (knots)
    if (aircraft_type ~ /Stealth/) {
        if (designation ~ /F-22/) max_speed = 1500
        else if (designation ~ /F-35/) max_speed = 1200
        else if (designation ~ /F-117/) max_speed = 617
        else if (designation ~ /B-2/) max_speed = 550
        else max_speed = 1000
    } else if (aircraft_type ~ /Interceptor/) {
        if (designation ~ /F-104/) max_speed = 1450
        else if (designation ~ /F-15/) max_speed = 1650
        else if (designation ~ /Lightning/) max_speed = 1500
        else max_speed = 1200 + (year - 1960) * 15
    } else if (aircraft_type ~ /Multi-Role|Strike/) {
        if (designation ~ /F-16/) max_speed = 1320
        else if (designation ~ /F\/A-18/) max_speed = 1190
        else if (designation ~ /Tornado/) max_speed = 1490
        else if (designation ~ /Typhoon/) max_speed = 1320
        else max_speed = 1100 + (year - 1970) * 10
    } else if (aircraft_type ~ /Jet Fighter/) {
        if (designation ~ /F-86/) max_speed = 687
        else if (designation ~ /F-100/) max_speed = 864
        else if (designation ~ /Meteor/) max_speed = 600
        else max_speed = 550 + (year - 1945) * 20
    } else if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        # WWII fighters
        if (designation ~ /P-51/) max_speed = 437
        else if (designation ~ /Spitfire/) max_speed = 378
        else if (designation ~ /Bf 109/) max_speed = 398
        else if (designation ~ /Zero/) max_speed = 351
        else max_speed = 300 + (year - 1940) * 10
    } else if (aircraft_type ~ /Bomber/) {
        if (designation ~ /B-52/) max_speed = 560
        else if (designation ~ /B-1/) max_speed = 900
        else if (designation ~ /B-2/) max_speed = 550
        else if (designation ~ /B-47/) max_speed = 580
        else if (designation ~ /Vulcan/) max_speed = 580
        else if (designation ~ /B-29/) max_speed = 300
        else max_speed = 250 + (year - 1940) * 8
    } else if (aircraft_type ~ /Attack/) {
        if (designation ~ /A-10/) max_speed = 381
        else max_speed = 500 + (year - 1960) * 15
    } else if (aircraft_type ~ /Transport/) {
        max_speed = 300 + (year - 1960) * 6
    } else if (aircraft_type ~ /Helo/) {
        if (designation ~ /AH-64/) max_speed = 158
        else if (designation ~ /UH-60/) max_speed = 159
        else max_speed = 120 + (year - 1960) * 1
    } else {
        max_speed = 400
    }

    # CRUISE SPEED (typically 65-75% of max speed)
    cruise_speed = int(max_speed * 0.70)

    # SERVICE CEILING (feet)
    if (aircraft_type ~ /Stealth|Interceptor|Multi-Role/) {
        ceiling = 50000 + (year - 1960) * 200
        if (ceiling > 65000) ceiling = 65000
    } else if (aircraft_type ~ /Jet Fighter/) {
        ceiling = 45000 + (year - 1945) * 150
    } else if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Jet/) {
        ceiling = 35000 + (year - 1940) * 200
    } else if (aircraft_type ~ /Bomber/) {
        ceiling = 40000 + (year - 1940) * 250
        if (ceiling > 50000) ceiling = 50000
    } else if (aircraft_type ~ /Transport/) {
        ceiling = 35000 + (year - 1960) * 100
    } else if (aircraft_type ~ /Helo/) {
        ceiling = 15000 + (year - 1960) * 50
        if (ceiling > 20000) ceiling = 20000
    } else {
        ceiling = 40000
    }

    # ENGINE TYPE
    if (aircraft_type ~ /Stealth|Interceptor|Multi-Role|Strike/) {
        engine_type = "Turbofan"
    } else if (aircraft_type ~ /Jet/) {
        engine_type = "Turbojet"
    } else if (aircraft_type ~ /Bomber/ && year > 1945) {
        if (designation ~ /B-52|Vulcan/) engine_type = "Turbojet"
        else if (year > 1980) engine_type = "Turbofan"
        else engine_type = "Turbojet"
    } else if (aircraft_type ~ /Transport/) {
        if (designation ~ /C-130|C-160|A400M/) engine_type = "Turboprop"
        else engine_type = "Turbofan"
    } else if (aircraft_type ~ /Helo/) {
        engine_type = "Turboshaft"
    } else {
        # WWII era
        engine_type = "Piston"
    }

    # NUMBER OF ENGINES
    if (designation ~ /P-38|F-14|F-15|F-22|F\/A-18|Meteor|Lightning|Typhoon|MiG-21/) {
        num_engines = 2
    } else if (designation ~ /B-17/) {
        num_engines = 4
    } else if (designation ~ /B-29|B-52/) {
        num_engines = 8
    } else if (designation ~ /B-47|Vulcan/) {
        num_engines = 4
    } else if (aircraft_type ~ /Bomber/ && year > 1960) {
        num_engines = 4
    } else if (aircraft_type ~ /Transport/) {
        num_engines = 4
    } else if (aircraft_type ~ /Helo/) {
        if (designation ~ /CH-47/) num_engines = 2
        else num_engines = 2
    } else {
        num_engines = 1
    }

    # CREW
    if (aircraft_type ~ /Fighter/ && aircraft_type !~ /Multi|Strike/) {
        if (designation ~ /F-14/) crew = 2
        else crew = 1
    } else if (aircraft_type ~ /Multi-Role|Strike|Interceptor/) {
        if (designation ~ /F-15E|F\/A-18F|Tornado/) crew = 2
        else crew = 1
    } else if (aircraft_type ~ /Stealth/) {
        crew = 1
    } else if (aircraft_type ~ /Bomber/) {
        if (designation ~ /B-17/) crew = 10
        else if (designation ~ /B-29/) crew = 11
        else if (designation ~ /B-52/) crew = 5
        else if (designation ~ /B-1/) crew = 4
        else if (designation ~ /B-2|B-21/) crew = 2
        else if (designation ~ /Vulcan/) crew = 5
        else crew = 3
    } else if (aircraft_type ~ /Attack/) {
        if (designation ~ /A-6/) crew = 2
        else crew = 1
    } else if (aircraft_type ~ /Transport/) {
        crew = 4
    } else if (aircraft_type ~ /Helo/) {
        if (designation ~ /AH-64|AH-1/) crew = 2
        else if (designation ~ /CH-47|CH-53/) crew = 3
        else crew = 2
    } else {
        crew = 1
    }

    # COMBAT RADIUS (nautical miles)
    if (aircraft_type ~ /Strategic Bomber/) {
        if (designation ~ /B-52/) combat_radius = 4480
        else if (designation ~ /B-1/) combat_radius = 3100
        else if (designation ~ /B-2|B-21/) combat_radius = 6000
        else combat_radius = 2000 + (year - 1950) * 80
    } else if (aircraft_type ~ /Bomber/ && aircraft_type !~ /Strategic/) {
        if (designation ~ /B-29/) combat_radius = 1600
        else if (designation ~ /Vulcan/) combat_radius = 2300
        else combat_radius = 800 + (year - 1940) * 30
    } else if (aircraft_type ~ /Interceptor|Multi-Role/) {
        if (designation ~ /F-15/) combat_radius = 1100
        else if (designation ~ /F-16/) combat_radius = 340
        else if (designation ~ /F\/A-18/) combat_radius = 410
        else combat_radius = 400 + (year - 1960) * 15
    } else if (aircraft_type ~ /Stealth/) {
        if (designation ~ /F-22/) combat_radius = 590
        else if (designation ~ /F-35/) combat_radius = 670
        else combat_radius = 600
    } else if (aircraft_type ~ /Fighter/) {
        combat_radius = 200 + (year - 1940) * 8
    } else if (aircraft_type ~ /Attack/) {
        combat_radius = 300 + (year - 1960) * 10
    } else if (aircraft_type ~ /Transport/) {
        combat_radius = 1500 + (year - 1960) * 30
    } else if (aircraft_type ~ /Helo/) {
        if (designation ~ /AH-64|AH-1/) combat_radius = 260
        else if (designation ~ /CH-47/) combat_radius = 200
        else combat_radius = 150 + (year - 1960) * 3
    } else {
        combat_radius = 400
    }

    # ROLE description
    if (aircraft_type ~ /Stealth Fighter/) {
        role = "Air superiority, strike missions"
    } else if (aircraft_type ~ /Interceptor/) {
        role = "Air defense, interception"
    } else if (aircraft_type ~ /Multi-Role/) {
        role = "Air-to-air and air-to-ground"
    } else if (aircraft_type ~ /Strike/) {
        role = "Ground attack, strike missions"
    } else if (aircraft_type ~ /Jet Fighter|^Fighter$/) {
        role = "Air superiority"
    } else if (aircraft_type ~ /Strategic Bomber/) {
        role = "Strategic bombing, long-range strike"
    } else if (aircraft_type ~ /Bomber|Dive Bomber/) {
        role = "Tactical bombing"
    } else if (aircraft_type ~ /Attack|V\/STOL Attack/) {
        role = "Close air support, ground attack"
    } else if (aircraft_type ~ /Transport/) {
        role = "Cargo transport, airlift"
    } else if (aircraft_type ~ /Tanker/) {
        role = "Aerial refueling"
    } else if (aircraft_type ~ /Attack Helo/) {
        role = "Anti-armor, close air support"
    } else if (aircraft_type ~ /Utility Helo/) {
        role = "Troop transport, utility"
    } else if (aircraft_type ~ /Transport Helo/) {
        role = "Heavy lift, cargo transport"
    } else if (aircraft_type ~ /EW|Recon/) {
        role = "Electronic warfare, reconnaissance"
    } else {
        role = "Multi-purpose operations"
    }

    # IS_MODDED (always 1 for database entries)
    is_modded = 1

    # Round values
    wingspan = sprintf("%.1f", wingspan)
    aircraft_length = sprintf("%.1f", aircraft_length)
    max_speed = int(max_speed)
    cruise_speed = int(cruise_speed)
    ceiling = int(ceiling)
    combat_radius = int(combat_radius)

    # Output database entry
    printf "| %s | %s | %s | %s | %s | %s | %s | %d | %d | %d | %d | %d | %s | %d | %d | %d | %s | %d | %s |\n",
        node_id, nation, designation, year, aircraft_type,
        wingspan, aircraft_length, max_weight, empty_weight,
        max_speed, cruise_speed, ceiling,
        engine_type, num_engines, crew, combat_radius,
        role, is_modded, modded
}
