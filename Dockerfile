# Start from the latest ROCm base image
FROM rocm/dev-ubuntu-22.04:6.0-complete

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set up a new user
RUN useradd -m -s /bin/bash user
USER user
WORKDIR /home/user/app

# Set up Python environment
ENV PATH="/home/user/.local/bin:${PATH}"
RUN python3 -m pip install --user --upgrade pip

COPY --chown=user:user requirements.txt .

# Switch to root user
USER root

# Install rocm-smi
RUN apt-get update && apt-get install -y rocm-smi

# Switch back to the non-root user
USER user


RUN pip install --user --no-cache-dir -r requirements.txt

# Copy the application code
COPY --chown=user:user . /home/user/app/

# Set an argument for the model path
ARG MODEL_PATH
ENV MODEL_PATH=${MODEL_PATH}

# Set the entry point to run the inference script
ENTRYPOINT ["python3", "src/run_inference.py"]