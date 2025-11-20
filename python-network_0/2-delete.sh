#!/bin/bash
# get the url

if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

url=$1

curl -s -X DELETE "$url"
