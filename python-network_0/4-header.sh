#!/bin/bash
# get request

if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

url=$1

curl -s -H "X-HolbertonSchool-User-Id: 98" "$url"
