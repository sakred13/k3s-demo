#!/bin/sh

echo "Enter text:"
read input

# Send text to worker2-pod for capitalization
curl -X POST http://edge2-service:80/capitalizeText -H "Content-Type: application/json" -d '{"text": "'"$input"'"}'

# Send text to master-pod
curl -X POST http://cloud-service:5000/unprocessedText -H "Content-Type: application/json" -d '{"text": "'"$input"'"}'
