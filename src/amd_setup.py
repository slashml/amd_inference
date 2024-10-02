import os
import torch

def setup_amd_environment():
    if torch.version.hip is None:
        print("This is not an AMD GPU environment. No setup needed.")
        return

    # Set environment variables for ROCm
    os.environ['HIP_VISIBLE_DEVICES'] = '0'  # Use the first GPU
    os.environ['HSA_OVERRIDE_GFX_VERSION'] = '11.0.0'  # Updated for newer AMD GPUs

    # Check if ROCm is properly set up
    try:
        assert torch.cuda.is_available()
        print(f"ROCm is properly set up. Using GPU: {torch.cuda.get_device_name(0)}")
    except AssertionError:
        print("Error: ROCm is not properly set up or no AMD GPU is available.")
        print("Please ensure that ROCm 6.2 is installed and configured correctly.")

def optimize_for_amd():
    if torch.version.hip is None:
        return

    # Set benchmark mode
    torch.backends.cudnn.benchmark = True

    # Enable TF32 for improved performance (if supported by the GPU)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

    print("Applied optimizations for AMD GPU with ROCm 6.2.")

# Call these functions when importing this module
setup_amd_environment()
optimize_for_amd()