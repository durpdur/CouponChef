import json

# Specify the path to the JSON file you want to open
file_path = "couponchef-dalle-backend/food_prices.json"  # Replace with the actual file path

# Open and read the JSON file
with open(file_path, "r") as json_file:
    data = json.load(json_file)
    
# Now, 'data' contains the parsed JSON data as a Python dictionary
print("JSON data:")
print(data)
