#!/bin/bash
# Gets the size of the body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
