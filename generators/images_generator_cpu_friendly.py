import os
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import time


def load_model(model_id="runwayml/stable-diffusion-v1-5", use_gpu=False):
    device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
    try:
        # CPU: float32, GPU: float16
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        pipe = pipe.to(device)
        print(f"Modell betöltve: {model_id} ({device})")
        return pipe
    except Exception as e:
        print("Hiba a modell betöltésekor:", str(e))
        return None


def generate_image(pipe, prompt, width=32, height=32, steps=10):
    if pipe is None:
        print("Modell nincs betöltve.")
        return None
    try:
        # CPU-barát: csökkentett lépésszám
        image = pipe(prompt, height=height, width=width, num_inference_steps=steps).images[0]
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
    start = time.time()

    pipe = load_model(use_gpu=False)  # CPU
    image = generate_image(pipe, prompt, width=128, height=128, steps=50)
    save_image(image)

    print(f"Futási idő: {time.time() - start:.2f} másodperc")


if __name__ == "__main__":
    main()