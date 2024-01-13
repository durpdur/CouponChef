import requests
import json
import os

# Spoonacular API
api_key = '78a05b1a5ac44c269140c0903cc0df75'
end_point = 'https://api.spoonacular.com/recipes/findByIngredients'
file_path = "food_prices.json"

recipes_list = []

try:
    with open(file_path, 'r') as file:
        data = json.load(file)

    names = ','.join([recipe.get('name', '') for recipe in data.get('groceryItems', [])])

    parameters = {
        'ingredients': names,
        'apiKey': api_key,
        'ignorePantry': False,
        'addRecipeNutrition': True
    }

    response = requests.get(end_point, params=parameters)
    sorted_recipes = sorted(response.json(), key=lambda x: x.get('missedIngredientCount', 0))

    # Desired nutrition fields
    desired_nutrition = ['Calories', 'Protein', 'Fiber', 'Fat', 'Carbohydrates', 'Sodium']

    for index, recipe in enumerate(sorted_recipes[:5]):
        # Get nutrition data
        nutrition_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe["id"]}/nutritionWidget.json', params={'apiKey': api_key})
        nutrition_data = nutrition_response.json()

        # Get recipe instructions
        recipe_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe["id"]}/information', params={'apiKey': api_key})
        recipe_data = recipe_response.json()
        instructions = recipe_data.get('analyzedInstructions', [{}])[0].get('steps', [])

        # Build recipe info
        recipe_info = {
            "title": recipe['title'],
            "image": recipe['image'],
            "usedIngredients": [item['name'] for item in recipe['usedIngredients']],
            "missedIngredients": [item['name'] for item in recipe['missedIngredients']],
            "nutrition": {nutrient["name"]: f"{nutrient['amount']} {nutrient['unit']}" for nutrient in nutrition_data.get('nutrients', []) if nutrient["name"] in desired_nutrition},
            "instructions": [f"Step {step['number']}: {step['step']}" for step in instructions]
        }
        recipes_list.append(recipe_info)

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Write to a JSON file
output_file = 'recipes_output.json'
with open(output_file, 'w') as file:
    json.dump(recipes_list, file, indent=4)

print(f"Saved top 5 recipes to {output_file}")

