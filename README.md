# ⚙️ AMD GPU Inference

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202-green.svg)](https://github.com/bentoml/OpenLLM/blob/main/LICENSE)
[![X](https://badgen.net/badge/icon/@slash_ml/000000?icon=twitter&label=Follow)](https://twitter.com/slash_ml)
[![Community](https://img.shields.io/discord/123456789012345678?logo=discord&label=Join%20Discord)](https://discord.com/invite/EXJkWygF)


This project provides a Docker-based inference engine for running Large Language Models (LLMs) on AMD GPUs. It's designed to work with models from Hugging Face, with a focus on the LLaMA model family.

## Prerequisites

- AMD GPU with ROCm support
- Docker installed on your system
- ROCm drivers installed on your host system (version 5.4.2 or compatible)

## Project Structure

```
amd-gpu-inference/
├── src/
│   ├── __init__.py
│   ├── engine.py
│   ├── model.py
│   ├── utils.py
│   └── amd_setup.py
├── Dockerfile
├── requirements.txt
├── run_inference.py
├── run-docker-amd.sh
└── README.md
```

## Quick Start

1. Clone this repository:
   ```
   git clone https://github.com/slashml/amd-gpu-inference.git
   cd amd-gpu-inference
   ```

2. Make the run script executable:
   ```
   chmod +x run-docker-amd.sh
   ```

3. Run the inference engine with a specified model and prompt:
   ```
   ./run-docker-amd.sh "meta-llama/Llama-2-7b-chat-hf" "Translate the following English text to French: 'Hello, how are you?'"
   ```
   Replace `"meta-llama/Llama-2-7b-chat-hf"` with the Hugging Face model you want to use, and provide your own prompt.

## Detailed Usage

### Aptfile

The project includes an `Aptfile` that lists the necessary ROCm packages to be installed in the Docker container. This ensures that all required ROCm drivers and libraries are available for the inference engine to utilize the AMD GPU effectively.

### Building the Docker Image

The `run-docker-amd.sh` script builds the Docker image automatically. If you want to build it manually, use:

```
docker build -t amd-gpu-inference .
```

### Running the Container

The `run-docker-amd.sh` script handles running the container with the necessary AMD GPU flags. If you want to run it manually:

```
docker run --rm -it \
    --device=/dev/kfd \
    --device=/dev/dri \
    --group-add=video \
    --cap-add=SYS_PTRACE \
    --security-opt seccomp=unconfined \
    amd-gpu-inference "model_name" "your prompt here"
```

Replace `"model_name"` with the Hugging Face model you want to use, and `"your prompt here"` with your input text.

## Customization

### Changing the Model

You can use any model available on Hugging Face by specifying its repository name when running the container. For example:

```
./run-docker-amd.sh "facebook/opt-1.3b" "Your prompt here"
```

### Modifying the Inference Logic

If you need to change how the inference is performed, modify the `run_inference.py` file. Remember to rebuild the Docker image after making changes.

## Troubleshooting

- Ensure that your AMD GPU drivers and ROCm are correctly installed and configured on your host system.
- If you encounter "out of memory" errors, try using a smaller model or reducing the input/output length.
- For model-specific issues, refer to the model's documentation on Hugging Face.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- This project uses the Hugging Face Transformers library.
- ROCm is developed by AMD. Licensed under MIT License
  See https://rocm.docs.amd.com/en/latest/about/license.html for details.

For any questions or issues, please open an issue in the GitHub repository.