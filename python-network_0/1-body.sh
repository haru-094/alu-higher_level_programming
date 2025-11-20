#!/bin/bash
# Display body of 200 status code response
curl -sL -w "%{http_code}" -o /tmp/body "$1" | grep -q "200" && cat /tmp/body
