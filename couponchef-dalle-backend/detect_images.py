import base64
import json
import requests
from openai import OpenAI

# OpenAI API Key
api_key = "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"


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = (
    "/Users/johnq/Documents/GitHub/CouponChef/couponchef-dalle-backend/image.png"
)

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Can you give me the items with the prices and units next to it?",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
    "max_tokens": 400,
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
)
listed_food = response.json()["choices"][0]["message"]["content"]

print(listed_food)

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant designed to output JSON.",
        },
        {
            "role": "user",
            "content": f"Please help me convert this response into JSON, where it is organized by groceryItems, name, price, and unit: {listed_food}",
        },
    ],
)

file_path = "../food_prices.json"
data = json.loads(response.json())
message_content = data["choices"][0]["message"]["content"]

with open(file_path, "w") as json_file:
    json.dump(json.loads(message_content), json_file, indent=4)
print(message_content)
