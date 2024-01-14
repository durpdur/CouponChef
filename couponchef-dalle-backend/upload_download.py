import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

app = Flask(__name__)
CORS(app)

load_dotenv()
api_key = os.environ.get("API_KEY")


@app.route("/upload", methods=["POST"])
@cross_origin()
def saveImage():
    uploaded_image = request.files["image"]

    if uploaded_image:
        image_data = uploaded_image.read()
        base64_image = base64.b64encode(image_data).decode("utf-8")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Can you give me the items with the prices next to it?",
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            "max_tokens": 300,
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

        return "Image received"

    else:
        return "No image file uploaded"


if __name__ == "__main__":
    app.run(port=5000)

