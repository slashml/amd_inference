from src.engine import InferenceEngine

def question_answering_example():
    model_path = "models/llama-2-1b"
    engine = InferenceEngine(model_path)

    context = "The Great Wall of China is an ancient wall in China. The wall is 6,259 km long and was built to protect the Chinese states and empires against nomadic invasions from the north. It was built from the 3rd century BC to the 17th century AD."
    question = "How long is the Great Wall of China?"

    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    result = engine.run_inference(prompt, max_length=50)

    print("Question Answering Example:")
    print(f"Context: {context}")
    print(f"Question: {question}")
    print(f"Answer: {result['output']}")
    print(f"Inference Time: {result['inference_time']}")

if __name__ == "__main__":
    question_answering_example()