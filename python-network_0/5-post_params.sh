#!/bin/bash
# post request

if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

url=$1

curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$url"
