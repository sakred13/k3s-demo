FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y curl jq && \
    rm -rf /var/lib/apt/lists/*

# Copy the sendText.sh script into the container
COPY sendText.sh /sendText.sh

# Make the script executable
RUN chmod +x /sendText.sh

# Define the entry point as a non-executing command
ENTRYPOINT ["sleep", "infinity"]
