#!/bin/bash
# Ship Research Tree to Naval Ships Database Converter
# Converts basic research tree data to detailed ship database format

# Function to estimate displacement based on ship type and year
estimate_displacement() {
    local ship_type=$1
    local year=$2

    case $ship_type in
        BB)
            if [ $year -lt 1906 ]; then echo 12000
            elif [ $year -lt 1915 ]; then echo 20000
            elif [ $year -lt 1922 ]; then echo 32000
            elif [ $year -lt 1936 ]; then echo 35000
            elif [ $year -lt 1945 ]; then echo 45000
            else echo 50000; fi ;;
        CV)
            if [ $year -lt 1930 ]; then echo 25000
            elif [ $year -lt 1940 ]; then echo 30000
            elif [ $year -lt 1945 ]; then echo 35000
            elif [ $year -lt 1960 ]; then echo 45000
            else echo 90000; fi ;;
        CA)
            if [ $year -lt 1920 ]; then echo 10000
            elif [ $year -lt 1945 ]; then echo 13000
            else echo 17000; fi ;;
        CL)
            if [ $year -lt 1920 ]; then echo 5000
            elif [ $year -lt 1945 ]; then echo 10000
            else echo 15000; fi ;;
        DD)
            if [ $year -lt 1920 ]; then echo 1000
            elif [ $year -lt 1945 ]; then echo 2000
            else echo 5000; fi ;;
        SS)
            if [ $year -lt 1920 ]; then echo 500
            elif [ $year -lt 1945 ]; then echo 1500
            else echo 3000; fi ;;
        *) echo 10000 ;;
    esac
}

# Function to estimate speed based on ship type and year
estimate_speed() {
    local ship_type=$1
    local year=$2

    case $ship_type in
        BB)
            if [ $year -lt 1906 ]; then echo 18
            elif [ $year -lt 1915 ]; then echo 21
            elif [ $year -lt 1936 ]; then echo 23
            else echo 30; fi ;;
        CV)
            if [ $year -lt 1940 ]; then echo 30
            else echo 33; fi ;;
        CA|CL)
            if [ $year -lt 1920 ]; then echo 25
            elif [ $year -lt 1945 ]; then echo 32
            else echo 33; fi ;;
        DD)
            if [ $year -lt 1920 ]; then echo 30
            elif [ $year -lt 1945 ]; then echo 35
            else echo 35; fi ;;
        SS)
            if [ $year -lt 1945 ]; then echo 15
            else echo 20; fi ;;
        *) echo 25 ;;
    esac
}

# Function to estimate range based on ship type
estimate_range() {
    local ship_type=$1

    case $ship_type in
        BB) echo 15000 ;;
        CV) echo 12000 ;;
        CA) echo 10000 ;;
        CL) echo 8000 ;;
        DD) echo 5000 ;;
        SS) echo 8000 ;;
        *) echo 10000 ;;
    esac
}

# Function to get Ship_ID based on country, ship_type, and node_id
get_ship_id() {
    local country=$1
    local ship_type=$2
    local node_id=$3

    case $country in
        USA)
            case $ship_type in
                BB) echo $((10000 + node_id)) ;;
                CV) echo $((11000 + node_id)) ;;
                CA) echo $((12000 + node_id)) ;;
                CL) echo $((12500 + node_id)) ;;
                DD) echo $((13000 + node_id)) ;;
                SS) echo $((15000 + node_id)) ;;
                *) echo $((10000 + node_id)) ;;
            esac ;;
        British)
            case $ship_type in
                BB) echo $((10100 + node_id)) ;;
                CV) echo $((11250 + node_id)) ;;
                CA) echo $((12100 + node_id)) ;;
                CL) echo $((12600 + node_id)) ;;
                DD) echo $((13300 + node_id)) ;;
                SS) echo $((15100 + node_id)) ;;
                *) echo $((10100 + node_id)) ;;
            esac ;;
        German)
            case $ship_type in
                BB) echo $((10200 + node_id)) ;;
                CV) echo $((11350 + node_id)) ;;
                CA) echo $((12150 + node_id)) ;;
                CL) echo $((12650 + node_id)) ;;
                DD) echo $((13400 + node_id)) ;;
                SS) echo $((15200 + node_id)) ;;
                *) echo $((10200 + node_id)) ;;
            esac ;;
        Japanese)
            case $ship_type in
                BB) echo $((10250 + node_id)) ;;
                CV) echo $((11350 + node_id)) ;;
                CA) echo $((12175 + node_id)) ;;
                CL) echo $((12675 + node_id)) ;;
                DD) echo $((13450 + node_id)) ;;
                SS) echo $((15250 + node_id)) ;;
                *) echo $((10250 + node_id)) ;;
            esac ;;
        *) echo $((10000 + node_id)) ;;
    esac
}

echo "Ship conversion script ready"
