# Start from the ROCm base image
FROM rocm/rocm-terminal:5.4.2

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/opt/rocm/bin:${PATH}"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src /app/src
COPY examples /app/examples

# Create a directory for the model
RUN mkdir -p /app/models

# Set an argument for the model path
ARG MODEL_PATH
ENV MODEL_PATH=${MODEL_PATH}

# Set the entry point to run the inference script
ENTRYPOINT ["python3", "src/run_inference.py"]

