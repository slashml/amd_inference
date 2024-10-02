#!/bin/bash

set -e

# Check if model name and prompt are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <model_name> <prompt>"
    echo "Example: $0 meta-llama/Llama-2-7b-chat-hf \"Translate the following English text to French: 'Hello, how are you?'\""
    exit 1
fi

MODEL_NAME="$1"
PROMPT="$2"

# Build the Docker image
echo "Building Docker image..."
docker build -t amd-gpu-inference .

# Run the container
echo "Running container with AMD GPU support..."
docker run --rm -it \
    --device=/dev/kfd \
    --device=/dev/dri \
    --group-add=video \
    --cap-add=SYS_PTRACE \
    --security-opt seccomp=unconfined \
    amd-gpu-inference "$MODEL_NAME" "$PROMPT"

echo "Container execution completed."