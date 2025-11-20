#!/bin/bash
# display the response

if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

url=$1

response=$(curl -s -w "%{http_code}" "$url")
body=${response::-3}
status=${response: -3}

if [ "$status" == "200" ]; then
    echo "$body"
fi
