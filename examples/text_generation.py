from src.engine import InferenceEngine

def text_generation_example():
    # You can change this to any supported LLaMA model on Hugging Face
    model_name = "meta-llama/Llama-3-8b"
    engine = InferenceEngine(model_name)

    prompt = "Write a short story about a robot learning to paint:"
    result = engine.run_inference(prompt, max_length=200)

    print("Text Generation Example:")
    print(f"Model: {model_name}")
    print(f"Prompt: {prompt}")
    print(f"Generated Story: {result['output']}")
    print(f"Inference Time: {result['inference_time']}")

if __name__ == "__main__":
    text_generation_example()