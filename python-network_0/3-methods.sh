#!/bin/bash
# display the url and the option

if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

url=$1

curl -s -X OPTIONS -i "$url" | grep -i Allow | cut -d' ' -f2-
