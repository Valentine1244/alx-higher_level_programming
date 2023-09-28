#!/bin/bash
# Gets body content
curl -sI "$1" | grep "Allow: " | cut -d' ' -f 2- 
