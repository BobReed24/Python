import torch
from diffusers import StableDiffusionPipeline
import argparse

def generate_image(prompt):
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v-1-4-original")
    pipe.to("cuda" if torch.cuda.is_available() else "cpu") 

    with torch.no_grad():
        image = pipe(prompt).images[0]

    image.save("generated_image.png")
    print("Image generated and saved as 'generated_image.png'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an image from a text prompt using Stable Diffusion.")
    parser.add_argument("prompt", type=str, help="Text prompt for generating the image")
    args = parser.parse_args()

    generate_image(args.prompt)
