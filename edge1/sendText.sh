#!/bin/sh

echo "Enter text:"
read input

# Construct JSON payload
json_payload=$(jq -n --arg input "$input" '{"text": $input}')

# Send text to worker2-pod for capitalization
curl -X POST http://edge2-service:80/capitalizeText -H "Content-Type: application/json" -d "$json_payload"

# Send text to master-pod
curl -X POST http://cloud-service:5000/unprocessedText -H "Content-Type: application/json" -d "$json_payload"

# curl -X GET http://cloud-service:5000/getTexts -H "Content-Type: application/json"