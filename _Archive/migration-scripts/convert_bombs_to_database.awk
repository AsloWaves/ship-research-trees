#!/usr/bin/awk -f
# Convert bomb research nodes to detailed naval_bombs_database format
# Input: bombs_extracted.tmp (19 fields)
# Output: naval_bombs_database.md format (23 fields)

BEGIN {
    FS = "|"
    OFS = "|"

    # Print header
    print "| Bomb_ID | Nation | Designation | Bomb_Type | Year | Weight | Length | Diameter | Explosive_Weight | Explosive_Type | Blast_Radius | Penetration | Guidance_Type | Guidance_Accuracy | Max_Range | Terminal_Velocity | Fuse_Type | Delivery_Platform | Cost_USD | Production_Years | Variants | Historical_Notes | Modded |"
    print "|---------|--------|-------------|-----------|------|--------|--------|----------|------------------|----------------|--------------|-------------|---------------|-------------------|-----------|-------------------|-----------|-------------------|----------|------------------|----------|------------------|--------|"
}

{
    # Skip empty lines
    if (NF < 10) next

    # Clean fields first
    for (i = 1; i <= NF; i++) {
        gsub(/^[ \t]+|[ \t]+$/, "", $i)
    }

    # Skip headers and empty lines after cleaning
    if ($2 ~ /Bomb_ID/ || $2 ~ /^-+$/ || $2 == "") next

    bomb_id = $2
    nation = $3
    designation = $4
    bomb_type = $5
    year = $6
    modded = $20

    # Weight estimation based on designation and type
    weight = estimate_weight(designation, bomb_type, nation)

    # Dimensions based on weight class
    bomb_length = estimate_length(weight, bomb_type)
    diameter = estimate_diameter(weight, bomb_type)

    # Explosive content
    explosive_weight = estimate_explosive_weight(weight, bomb_type, year)
    explosive_type = estimate_explosive_type(year, bomb_type, nation)

    # Blast characteristics
    blast_radius = estimate_blast_radius(explosive_weight, explosive_type)
    penetration = estimate_penetration(weight, bomb_type, designation)

    # Guidance system
    guidance_type = estimate_guidance_type(bomb_type, designation, year)
    guidance_accuracy = estimate_guidance_accuracy(guidance_type, year)
    max_range = estimate_max_range(bomb_type, weight, guidance_type)

    # Delivery characteristics
    terminal_velocity = estimate_terminal_velocity(weight, bomb_type)
    fuse_type = estimate_fuse_type(bomb_type, designation)
    delivery_platform = estimate_delivery_platform(weight, year, nation)

    # Cost and production
    cost_usd = estimate_cost(bomb_type, guidance_type, year, weight)
    production_years = estimate_production_years(year, nation, designation)

    # Variants and notes
    variants = estimate_variants(designation, bomb_type, nation)
    historical_notes = generate_historical_notes(designation, bomb_type, year, nation)

    # Output full database entry
    printf "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n",
        bomb_id, nation, designation, bomb_type, year,
        weight, bomb_length, diameter, explosive_weight, explosive_type,
        blast_radius, penetration, guidance_type, guidance_accuracy, max_range,
        terminal_velocity, fuse_type, delivery_platform, cost_usd, production_years,
        variants, historical_notes, modded
}

function estimate_weight(desig, type, nation,    w) {
    # Extract weight from designation
    if (desig ~ /250 lb/) return 113
    if (desig ~ /500 lb/) return 227
    if (desig ~ /1000 lb/) return 454
    if (desig ~ /2000 lb/) return 907
    if (desig ~ /4000 lb/) return 1814
    if (desig ~ /250 kg/) return 250
    if (desig ~ /500 kg/) return 500
    if (desig ~ /1000 kg/) return 1000

    # Standard bomb series
    if (desig ~ /Mk 81/) return 113
    if (desig ~ /Mk 82/) return 227
    if (desig ~ /Mk 83/) return 447
    if (desig ~ /Mk 84/) return 907
    if (desig ~ /AN-M30/) return 45
    if (desig ~ /AN-M64/) return 227
    if (desig ~ /AN-M65/) return 454
    if (desig ~ /AN-M66/) return 907

    # GBU series (based on base bomb + guidance kit)
    if (desig ~ /GBU-10/) return 960  # Paveway I on Mk 84
    if (desig ~ /GBU-12/) return 240  # Paveway II on Mk 82
    if (desig ~ /GBU-16/) return 460  # Paveway II on Mk 83
    if (desig ~ /GBU-24/) return 1020 # Paveway III on Mk 84
    if (desig ~ /GBU-28/) return 2130 # BLU-113 + guidance
    if (desig ~ /GBU-31/) return 930  # JDAM on Mk 84
    if (desig ~ /GBU-32/) return 470  # JDAM on Mk 83
    if (desig ~ /GBU-38/) return 240  # JDAM on Mk 82
    if (desig ~ /GBU-39/) return 130  # SDB
    if (desig ~ /GBU-53/) return 115  # SDB II
    if (desig ~ /GBU-54/) return 240  # LJDAM on Mk 82
    if (desig ~ /GBU-56/) return 470  # LJDAM on Mk 83
    if (desig ~ /GBU-57/) return 13600 # MOP

    # Famous British bombs
    if (desig ~ /Tallboy/) return 5440
    if (desig ~ /Grand Slam/) return 9980

    # German bombs
    if (desig ~ /SC 50/) return 50
    if (desig ~ /SC 250/) return 250
    if (desig ~ /SC 500/) return 500
    if (desig ~ /SC 1000/) return 1000
    if (desig ~ /SC 1800/) return 1800
    if (desig ~ /PC 1400/) return 1400
    if (desig ~ /Fritz X/) return 1400
    if (desig ~ /Hs 293/) return 650

    # Nuclear bombs (total weapon weight)
    if (desig ~ /Mk 4/) return 4900
    if (desig ~ /Mk 7/) return 780
    if (desig ~ /Mk 15/) return 3400
    if (desig ~ /Mk 28/) return 980
    if (desig ~ /Mk 43/) return 970
    if (desig ~ /B57/) return 230
    if (desig ~ /B61/) return 320
    if (desig ~ /B83/) return 1090
    if (desig ~ /Blue Danube/) return 4500
    if (desig ~ /Red Beard/) return 900
    if (desig ~ /WE.177/) return 270

    # Cluster munitions
    if (desig ~ /CBU-87/) return 430
    if (desig ~ /CBU-97/) return 430
    if (desig ~ /CBU-103/) return 430
    if (desig ~ /CBU-105/) return 430
    if (desig ~ /BL755/) return 264
    if (desig ~ /RBL755/) return 264

    # Default by type
    if (type ~ /Heavy Bomb/) return 2000
    if (type ~ /Penetrator/) return 900
    if (type ~ /Cluster/) return 400
    if (type ~ /Nuclear/) return 500
    if (type ~ /Incendiary/) return 350
    return 250  # Default GP bomb
}

function estimate_length(weight, type,    len) {
    # Nuclear bombs are shorter for same weight
    if (type ~ /Nuclear/) return sprintf("%.2f", 2.5 + (weight / 1000) * 0.5)

    # Cluster munitions are longer, thinner
    if (type ~ /Cluster/) return sprintf("%.2f", 2.2 + (weight / 300))

    # Heavy bombs are longer
    if (type ~ /Heavy/) return sprintf("%.2f", 3.0 + (weight / 800))

    # Glide bombs have wings
    if (type ~ /Glide/) return sprintf("%.2f", 3.5 + (weight / 400))

    # Standard bombs: roughly 3-4m for 500kg
    return sprintf("%.2f", 1.5 + (weight / 200))
}

function estimate_diameter(weight, type,    diam) {
    if (type ~ /Nuclear/) return sprintf("%.3f", 0.35 + (weight / 3000))
    if (type ~ /Cluster/) return sprintf("%.3f", 0.30 + (weight / 1500))
    if (type ~ /Heavy/) return sprintf("%.3f", 0.40 + (weight / 3000))

    # Standard formula: diameter increases with cube root of weight
    return sprintf("%.3f", 0.20 + (weight / 1000) ** 0.33 * 0.15)
}

function estimate_explosive_weight(weight, type, year,    ratio) {
    # Nuclear bombs don't have HE fill
    if (type ~ /Nuclear/) return 0

    # Incendiary bombs have lower HE content
    if (type ~ /Incendiary/) return int(weight * 0.30)

    # Penetrators have thicker casings
    if (type ~ /Penetrator/) return int(weight * 0.40)
    if (type ~ /AP Bomb/) return int(weight * 0.35)

    # Modern bombs have higher fill ratios
    if (year >= 1980) ratio = 0.55
    else if (year >= 1960) ratio = 0.50
    else ratio = 0.45

    # Cluster munitions
    if (type ~ /Cluster/) return int(weight * 0.40)

    return int(weight * ratio)
}

function estimate_explosive_type(year, type, nation) {
    # Nuclear bombs
    if (type ~ /Nuclear/) {
        if (year >= 1960) return "Thermonuclear"
        else return "Fission"
    }

    # Incendiary
    if (type ~ /Incendiary/) return "Napalm"

    # Modern era
    if (year >= 2000) return "PBXN-109"
    if (year >= 1980) return "H6"
    if (year >= 1960) return "Comp B"

    # WWII era by nation
    if (nation ~ /German/) return "Amatol"
    if (nation ~ /British/) return "RDX/TNT"
    return "Tritonal"
}

function estimate_blast_radius(exp_weight, exp_type,    base_radius) {
    if (exp_weight == 0) {
        # Nuclear weapons - assume tactical yield
        return 1500  # 1.5km blast radius
    }

    # Base radius from explosive weight (meters)
    base_radius = int(exp_weight ** 0.4 * 15)

    # Modifier for explosive type
    if (exp_type ~ /H6/) base_radius = int(base_radius * 1.15)
    if (exp_type ~ /PBXN/) base_radius = int(base_radius * 1.10)
    if (exp_type ~ /Napalm/) base_radius = int(base_radius * 1.30)

    return base_radius
}

function estimate_penetration(weight, type, desig,    pen) {
    if (type !~ /Penetrator/ && type !~ /AP Bomb/ && type !~ /Bunker/) return 0

    # Penetration roughly proportional to weight and kinetic energy
    pen = int(weight * 0.8)  # mm of RHA equivalent

    # Special cases
    if (desig ~ /GBU-28/) return 6000   # 30ft concrete or 100ft earth
    if (desig ~ /GBU-57/) return 60000  # 200ft reinforced concrete
    if (desig ~ /BLU-109/) return 1800
    if (desig ~ /BLU-116/) return 2400
    if (desig ~ /PC 1400/) return 1400
    if (desig ~ /Type 91/) return 250

    return pen
}

function estimate_guidance_type(type, desig, year) {
    if (type ~ /LGB/) return "Laser"
    if (type ~ /GPS-Guided/) return "GPS+INS"
    if (type ~ /Laser\/GPS/ || type ~ /Dual-Mode/) return "Laser+GPS"
    if (type ~ /TV-Guided/) return "TV"
    if (desig ~ /Fritz X/) return "Radio"
    if (desig ~ /Hs 293/) return "Radio+Rocket"

    # Unguided
    return "None"
}

function estimate_guidance_accuracy(guid_type, year,    cep) {
    if (guid_type == "None") return 200

    # Technology progression
    if (guid_type ~ /Laser\+GPS/) {
        if (year >= 2010) return 3
        return 5
    }

    if (guid_type ~ /GPS/) {
        if (year >= 2010) return 8
        if (year >= 2000) return 10
        return 13
    }

    if (guid_type ~ /Laser/) {
        if (year >= 2000) return 4
        if (year >= 1980) return 6
        return 10
    }

    if (guid_type ~ /TV/) return 15
    if (guid_type ~ /Radio/) return 50

    return 200
}

function estimate_max_range(type, weight, guid,    range_km) {
    # Unguided bombs have minimal range
    if (guid == "None") return 5

    # Powered glide bombs
    if (type ~ /Powered/) return 120
    if (type ~ /Extended Range/) return 80

    # Glide bombs with wings
    if (type ~ /Glide/) return 15

    # Standard guided bombs (glide from altitude)
    if (guid ~ /GPS/ || guid ~ /Laser/) {
        if (weight > 1000) return 25
        if (weight > 400) return 20
        return 15
    }

    return 10
}

function estimate_terminal_velocity(weight, type,    vel) {
    # Heavier bombs fall faster
    vel = int(150 + (weight / 500) * 50)

    # Retarded/cluster bombs fall slower
    if (type ~ /Cluster/) vel = int(vel * 0.6)

    # Cap at supersonic for heavy penetrators
    if (vel > 350) vel = 350

    return vel
}

function estimate_fuse_type(type, desig) {
    if (type ~ /Nuclear/) return "Airburst/Ground"
    if (type ~ /Penetrator/ || type ~ /Bunker/) return "Delayed"
    if (type ~ /AP Bomb/) return "Delayed"
    if (type ~ /Cluster/) return "Proximity"
    if (type ~ /Mine/) return "Magnetic/Acoustic"
    if (type ~ /Incendiary/) return "Impact"

    # Default GP bomb
    return "Contact/Delay"
}

function estimate_delivery_platform(weight, year, nation,    platform) {
    if (weight > 5000) return "Heavy Bomber"
    if (weight > 1500) return "Bomber"
    if (weight > 500) {
        if (year >= 1970) return "Multirole Fighter"
        return "Fighter-Bomber"
    }
    if (year >= 1980) return "Fighter/Attack"
    return "Attack Aircraft"
}

function estimate_cost(type, guid, year, weight,    base_cost) {
    # Base cost by era and type
    if (type ~ /Nuclear/) {
        if (year >= 2000) return 28000000
        if (year >= 1980) return 15000000
        return 8000000
    }

    # Unguided bombs
    if (guid == "None") {
        if (year >= 1980) base_cost = 3000 + (weight * 30)
        else base_cost = 2000 + (weight * 20)
        return int(base_cost)
    }

    # Guidance kit costs
    if (guid ~ /Laser\+GPS/) base_cost = 60000
    else if (guid ~ /GPS/) base_cost = 25000
    else if (guid ~ /Laser/) base_cost = 30000
    else if (guid ~ /TV/) base_cost = 50000
    else if (guid ~ /Radio/) base_cost = 15000

    # Add base bomb cost
    base_cost += (weight * 40)

    # Special cases
    if (type ~ /Penetrator/) base_cost *= 1.5
    if (type ~ /Cluster/) base_cost *= 1.3
    if (type ~ /Powered/) base_cost *= 2.0

    return int(base_cost)
}

function estimate_production_years(year, nation, desig,    end_year) {
    # Nuclear weapons typically 20-30 year service life
    if (desig ~ /Nuclear/ || desig ~ /Mk [0-9]/ || desig ~ /B61/ || desig ~ /B83/) {
        end_year = year + 25
        if (end_year > 2025) end_year = 2025
        return year "-" end_year
    }

    # WWII weapons
    if (year < 1950) {
        end_year = year + 10
        if (end_year > 1955) end_year = 1955
        return year "-" end_year
    }

    # Cold War weapons
    if (year < 1980) {
        end_year = year + 20
        if (end_year > 2025) end_year = 2025
        return year "-" end_year
    }

    # Modern weapons still in production
    if (year >= 2000) return year "-Present"

    # 1980s-1990s weapons
    end_year = year + 30
    if (end_year > 2025) end_year = 2025
    return year "-" end_year
}

function estimate_variants(desig, type, nation,    var) {
    # USA GBU series variants
    if (desig ~ /GBU-12/) return "GBU-12A/B/C/D, Paveway II"
    if (desig ~ /GBU-24/) return "GBU-24A/B, Paveway III"
    if (desig ~ /GBU-31/) return "GBU-31(V)1/2/3/4"
    if (desig ~ /GBU-38/) return "GBU-38(V)1/2/3"
    if (desig ~ /B61/) return "B61-3/4/7/10/11/12"

    # Mk series
    if (desig ~ /Mk 82/) return "Mk 82, BSU-86 Snakeye"
    if (desig ~ /Mk 83/) return "Mk 83, BSU-85 Snakeye"
    if (desig ~ /Mk 84/) return "Mk 84, BSU-50"

    # British
    if (desig ~ /Paveway IV/) return "Paveway IV, Dual Mode"
    if (desig ~ /WE.177/) return "WE.177A/B/C"

    return "Standard"
}

function generate_historical_notes(desig, type, year, nation,    notes) {
    # Famous weapons
    if (desig ~ /Tallboy/) return "Barnes Wallis earthquake bomb, 12,000 lb, penetrated 16ft concrete"
    if (desig ~ /Grand Slam/) return "Largest conventional bomb of WWII, 22,000 lb, earthquake bomb"
    if (desig ~ /Fritz X/) return "First operational guided bomb, sank Italian battleship Roma 1943"
    if (desig ~ /Hs 293/) return "First glide bomb, rocket-boosted, anti-ship weapon"
    if (desig ~ /GBU-28/) return "Bunker buster, used in Gulf War 1991 against hardened targets"
    if (desig ~ /GBU-57/) return "Massive Ordnance Penetrator, largest conventional penetrator"
    if (desig ~ /B61-12/) return "Modern guided nuclear bomb, variable yield, high precision"
    if (desig ~ /Type 91/) return "Modified 16-inch naval shell, used at Pearl Harbor"
    if (desig ~ /Blue Danube/) return "Britain's first operational nuclear weapon"
    if (desig ~ /SPEAR 3/) return "Network-enabled powered glide bomb, 150km range"

    # Type-based notes
    if (type ~ /GPS-Guided/ && year < 2000) return "Early JDAM system, revolutionized precision bombing"
    if (type ~ /LGB/ && year < 1980) return "Early laser-guided bomb, Vietnam War era"
    if (type ~ /Nuclear/ && year < 1960) return "First-generation nuclear weapon, large warhead"
    if (type ~ /Cluster/ && year < 1990) return "Area effect munition, anti-personnel/armor"

    return "Standard operational bomb"
}
