import os
import torch

def setup_amd_environment():
    """Set up the environment for AMD GPUs."""
    if torch.version.hip is None:
        print("This is not an AMD GPU environment. No setup needed.")
        return

    # Set environment variables for ROCm
    os.environ['HIP_VISIBLE_DEVICES'] = '0'  # Use the first GPU
    os.environ['HSA_OVERRIDE_GFX_VERSION'] = '10.3.0'  # Set the GPU architecture version

    # Check if ROCm is properly set up
    try:
        assert torch.cuda.is_available()
        print(f"ROCm is properly set up. Using GPU: {torch.cuda.get_device_name(0)}")
    except AssertionError:
        print("Error: ROCm is not properly set up or no AMD GPU is available.")
        print("Please ensure that ROCm is installed and configured correctly.")

def optimize_for_amd():
    """Apply optimizations for AMD GPUs."""
    if torch.version.hip is None:
        return

    # Set benchmark mode
    torch.backends.cudnn.benchmark = True

    # Other AMD-specific optimizations can be added here
    # For example, you might want to set specific flags or use AMD-optimized libraries

    print("Applied optimizations for AMD GPU.")

# Call these functions when importing this module
setup_amd_environment()
optimize_for_amd()