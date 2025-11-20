#!/bin/bash
# display the response
[ $# -eq 1 ] || { echo "Usage: $0 URL"; exit 1; }
rc=$(curl -s -L -o /dev/null -w "%{redirect_count}" "$1"); [ "$rc" -eq 0 ] && echo "no redirection" || echo "$rc redirection"