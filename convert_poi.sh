#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    read -r SYS
    read -r PL
    read -r LAT
    read -r LON
    read -r AUT
    echo "places.append(\"${line} ${SYS} ${PL} ${LAT} ${LON} (${AUT})\")"
done < "POI_from_hotdoy.ca"