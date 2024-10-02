import random
import torch
import numpy as np

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def format_time(time_ms):
    """Convert time from milliseconds to a human-readable format."""
    if time_ms < 1000:
        return f"{time_ms:.2f}ms"
    elif time_ms < 60000:
        return f"{time_ms/1000:.2f}s"
    else:
        minutes = int(time_ms / 60000)
        seconds = (time_ms % 60000) / 1000
        return f"{minutes}m {seconds:.2f}s"

def get_gpu_memory_usage():
    """Get the current GPU memory usage."""
    if torch.cuda.is_available():
        return torch.cuda.memory_allocated() / 1024**2  # Convert to MB
    else:
        return 0

def print_gpu_utilization():
    """Print current GPU utilization."""
    if torch.cuda.is_available():
        if torch.version.hip is not None:
            print(f"AMD GPU Memory Usage: {get_gpu_memory_usage():.2f} MB")
        else:
            print(f"NVIDIA GPU Memory Usage: {get_gpu_memory_usage():.2f} MB")
    else:
        print("CUDA is not available. Running on CPU.")

def is_amd_gpu():
    """Check if the current GPU is an AMD GPU."""
    return torch.cuda.is_available() and torch.version.hip is not None

def get_gpu_info():
    """Get information about the current GPU."""
    if not torch.cuda.is_available():
        return "No GPU available"
    
    if is_amd_gpu():
        return f"AMD GPU: {torch.cuda.get_device_name(0)}"
    else:
        return f"NVIDIA GPU: {torch.cuda.get_device_name(0)}"