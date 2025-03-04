try:
    from gpt4all import GPT4All
    import torch
    from diffusers import StableDiffusionPipeline
except ImportError as e:
    print(f"Error importing libraries: {e}")
    exit()

print("1. Chat prompt")
print("2. Image Generation")
operand = input(">: ")

if operand == '1':
    try:
        model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
    except Exception as e:
        print(f"Error initializing chat model: {e}")
        exit()

elif operand == '2':
    model_id = "CompVis/stable-diffusion-v1-4"
    try:
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        if torch.cuda.is_available():
            pipe = pipe.to("cuda")
        else:
            print("CUDA is not available. Please use a CPU-compatible model.")
            exit()
    except Exception as e:
        print(f"Error initializing image generation model: {e}")
        exit()

else:
    print("Invalid choice!")
    exit()

try:
    with model.chat_session() as session:
        res = input("Enter your prompt: ")

        response = model.generate(res, max_tokens=1024)

        if operand == '1':

            if isinstance(response, str):
                with open("output.txt", "w") as f:
                    f.write(response)
                print("Response saved to output.txt")
            else:
                print("Error: Response is not a valid string.")

        elif operand == '2':
            with torch.no_grad():
                image = pipe(res).images[0]  

            image.save("output.png")
            print("Image generated and saved as 'output.png'")

except Exception as e:
    print(f"An error occurred: {e}")
