import base64
import json
import requests

class DetectImages:
  def __init__(self):
    pass
  
  # OpenAI API Key
  api_key = "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"

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Can you give me the items with the prices next to it?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  file_path = "couponchef-dalle-backend/food_prices.json"
  with open(file_path, "w") as json_file:
      json.dump(response.json(), json_file, indent=4)
  print(response.json())