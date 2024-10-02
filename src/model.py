import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class LlamaModel:
    def __init__(self, model_name):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if self.device.type == "cuda" and torch.version.hip is not None:
            print("Using AMD GPU with ROCm")
        elif self.device.type == "cuda":
            print("Using NVIDIA GPU")
        else:
            print("Using CPU")

        print(f"Loading model {model_name} from Hugging Face...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16).to(self.device)
        print("Model loaded successfully.")

    def generate(self, prompt, max_length=100, temperature=0.7):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            output = self.model.generate(
                input_ids,
                max_length=max_length,
                temperature=temperature,
                num_return_sequences=1,
                do_sample=True,
                top_p=0.95,
            )
        
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text

    def __call__(self, prompt, **kwargs):
        return self.generate(prompt, **kwargs)