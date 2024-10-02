import torch
from .model import LlamaModel
from .utils import set_seed, format_time

class InferenceEngine:
    def __init__(self, model_path, seed=42):
        set_seed(seed)
        self.model = LlamaModel(model_path)
        self.is_amd_gpu = torch.version.hip is not None

    def run_inference(self, prompt, max_length=100, temperature=0.7):
        if self.is_amd_gpu:
            start_event = torch.cuda.Event(enable_timing=True)
            end_event = torch.cuda.Event(enable_timing=True)
            start_event.record()
        else:
            start_time = torch.cuda.Event(enable_timing=True)
            end_time = torch.cuda.Event(enable_timing=True)
            start_time.record()

        output = self.model(prompt, max_length=max_length, temperature=temperature)

        if self.is_amd_gpu:
            end_event.record()
            torch.cuda.synchronize()
            inference_time = start_event.elapsed_time(end_event)
        else:
            end_time.record()
            torch.cuda.synchronize()
            inference_time = start_time.elapsed_time(end_time)

        return {
            "input": prompt,
            "output": output,
            "inference_time": format_time(inference_time)
        }

    def batch_inference(self, prompts, **kwargs):
        results = []
        for prompt in prompts:
            results.append(self.run_inference(prompt, **kwargs))
        return results