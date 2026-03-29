import os
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import time

def load_model(model_id="runwayml/stable-diffusion-v1-5", use_gpu=True):
    try:
        device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device=="cuda" else torch.float32)
        pipe = pipe.to(device)
        print(f"Modell betöltve: {model_id} ({device})")
        return pipe
    except Exception as e:
        print("Hiba a modell betöltésekor:", str(e))
        return None

def generate_image(pipe, prompt, width=512, height=512):
    if pipe is None:
        print("Modell nincs betöltve.")
        return None
    try:
        image = pipe(prompt, height=height, width=width).images[0]
        return image
    except Exception as e:
        print("Hiba a kép generálásakor:", str(e))
        return None

def save_image(image, folder="content/pictures"):
    if image is None:
        print("Nincs kép, amit elmenthetnénk.")
        return None
    try:
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, f"image_{int(time.time())}.png")
        image.save(filename)
        print("Kép mentve ide:", filename)
        return filename
    except Exception as e:
        print("Hiba a kép mentésekor:", str(e))
        return None

def main():
    prompt = input("Adj meg egy promptot: ")
    pipe = load_model(use_gpu=True)
    image = generate_image(pipe, prompt)
    save_image(image)

if __name__ == "__main__":
    main()