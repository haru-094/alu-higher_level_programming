#!/bin/bash
# Script to display the size of response

if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

url=$1

size=$(curl -s -w "%{size_download}" -o /dev/null "$url")
echo "$size"
