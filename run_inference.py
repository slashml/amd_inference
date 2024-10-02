import os
import sys
from src.engine import InferenceEngine
from src.utils import print_gpu_utilization, get_gpu_info

def run_inference(model_name, prompt):
    print(f"GPU Info: {get_gpu_info()}")
    print_gpu_utilization()


    print(f"Initializing inference engine...")
    print(f"GPU Info: {get_gpu_info()}")
    print_gpu_utilization()

    engine = InferenceEngine(model_name)

    result = engine.run_inference(prompt, max_length=200)

    print(f"Input: {result['input']}")
    print(f"Output: {result['output']}")
    print(f"Inference Time: {result['inference_time']}")

    print_gpu_utilization()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = "Explain the concept of machine learning in simple terms."
    
    run_inference(prompt)