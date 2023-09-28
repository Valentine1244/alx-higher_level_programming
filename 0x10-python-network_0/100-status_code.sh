#!/bin/bash
# Gets body content
curl -sI -w '%{response_code}' "$1" -o /dev/null
