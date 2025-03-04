import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model and tokenizer
model_name = "gpt-4-all"  # Replace with the actual model name if needed
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

# Prepare input
input_text = "Once upon a time"
inputs = tokenizer(input_text, return_tensors="pt").to(device)

# Generate output
with torch.no_grad():
    outputs = model.generate(**inputs, max_length=50)

# Decode the output
output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(output_text)
