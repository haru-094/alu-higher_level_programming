#!/bin/bash
# Script to display the size of response body in bytes
curl -sI "$1" | grep -i Content-Length | cut -d' ' -f2