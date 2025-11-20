#!/bin/bash
# display
[ $# -eq 1 ] || { echo "Usage: $0 URL"; exit 1; }
rc=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE "$1"); case "$rc" in 2*) echo "route accept DELETE method" ;; *) echo "route doesn't accept DELETE method" ;; esac