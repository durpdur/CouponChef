import requests
import json

#json stuff
# insert directory???
file_path = '/Users/laurenceliao/Documents/GitHub/CouponChef/food_prices.json'


#spoonacular stuff
api_key = ''
end_point = 'https://api.spoonacular.com/recipes/findByIngredients'

# print the contents of json file

names = ''
recipes_list = []
try:
    with open(file_path, 'r') as file:
        data = json.load(file)

    for recipe in data.get('groceryItems', []):
        #print(recipe['name'])
        #gets the names of all the items for recipes
        names += recipe.get('name', '') + ','

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

names = names.rstrip(',')
#print(names)


parameters = {
    'ingredients': names,
    'apiKey': api_key,
    'ignorePantry': False
}

# Make the API request
response = requests.get(f'{end_point}', params=parameters)
data = response.json()

'''
indented_json_string = json.dumps(response.json(), indent=2)
print(indented_json_string)
'''

# Sort recipes based on the number of ingredients

sorted_recipes = sorted(data, key=lambda x: x.get('missedIngredientCount', 0), reverse=False)

all_recipes = []
#display the top three recipes, nutrition, and recipes
for index, recipe in enumerate(sorted_recipes[:3]):
    
    title = recipe['title']
    missed_ingredients_count = recipe.get('missedIngredientCount', 0)
    missed_ingredients = recipe.get('missedIngredients', [])
    used_ingredients = recipe.get('usedIngredients', [])
    

    print(f"{index + 1}. {title} (MissedIngredientCount: {missed_ingredients_count})")
    print()
    print(" These are the ingredients you have:", ", ".join(ingredient['name'] for ingredient in used_ingredients))
    print()
    print(" These are the ingredients you are missing:", ", ".join(ingredient['name'] for ingredient in missed_ingredients))
    print()

    # Nutrients for the current recipe
    desired_nutrition = ['Calories', 'Protein', 'Fiber', 'Fat', 'Carbohydrates', 'Sodium']
    recipe_id = recipe['id']

    nutrition_parameters = {
        'id': recipe_id,
        'apiKey': api_key
    }

    nutrition_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json', params=nutrition_parameters)
    nutrition_data = nutrition_response.json()
    nutrients_data = nutrition_data.get('nutrients', [])

    # Iterate Through Desired Nutrients
    for nutrient in desired_nutrition:
        # Find Matching Nutrient in 'nutrients' Data
        matching_nutrients = [item for item in nutrients_data if item['name'].lower() == nutrient.lower()]

        # Display Nutrient Information
        if matching_nutrients:
            nutrient_info = matching_nutrients[0]
            amount = nutrient_info.get('amount')
            unit = nutrient_info.get('unit')
            print(f"  {nutrient.capitalize()}: {amount} {unit}")
        else:
            print(f"  {nutrient.capitalize()} not found in nutrients data.")

    print()

    #Lists out the recipe steps
    recipe_parameters = {
        'api-key': api_key,
        'stepBreakdown': True
    }
    recipe_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/information', params=parameters)
    recipe_data = recipe_response.json()
    steps_data = recipe_data.get('analyzedInstructions', [{'steps': []}])

    if 'analyzedInstructions' in recipe_data:
        for step in recipe_data['analyzedInstructions'][0]['steps']:
            print(f"Step {step['number']}: {step['step']}")

    else:
        print("No steps found for this recipe.")
    
    print()

    current_recipe_info = {
        'title': f"{index + 1}. {title} (MissedIngredientCount: {missed_ingredients_count})",
        'usedIngredients': [ingredient['name'] for ingredient in used_ingredients],
        'missingIngredients': [ingredient['name'] for ingredient in missed_ingredients],
        'Nutrition': [{nutrient['name']: {'amount': nutrient['amount'], 'unit': nutrient['unit']}} for nutrient in nutrients_data if nutrient['name'] in desired_nutrition],
        'Steps': [step['step'] for step in steps_data[0]['steps']]
    }

    all_recipes.append(current_recipe_info)


json_object = json.dumps(all_recipes, indent=4)
 
# Writing to sample.json
with open("email.json", "w") as outfile:
    outfile.write(json_object)
    
    


