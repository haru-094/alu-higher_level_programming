#!/bin/bash
# Script to display the size of response
[ $# -eq 1 ] && curl -s -o /dev/null -w "%{size_download}\n" "$1"
[ $# -ne 1 ] && echo "Usage: $0 URL"
