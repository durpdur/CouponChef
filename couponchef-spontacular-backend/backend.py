import requests
import json

#json stuff
# insert directory???
file_path = '/Users/laurenceliao/Documents/GitHub/CouponChef/couponchef-spontacular-backend/sample_food_prices.json'


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
print(names)


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

# Display the top 5 recipes
for index, recipe in enumerate(sorted_recipes[:5]):
    print(f"{index + 1}. {recipe['title']} (MissedIngredientCount: {recipe.get('missedIngredientCount', 0)})")

top_five = sorted_recipes[:5]
for id in top_five:
    print(id['id'])

# Nutrients for the top 5 recipes
desired_nutrition = ['Calories', 'Protein', 'Fiber', 'Fat', 'Carbohydrates', 'Sodium']
for id in top_five:
    recipe_id = id['id']
    nutrition_parameters = {
        'id': recipe_id,
        'apiKey': api_key
    }

    nutrition_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json', params=nutrition_parameters)
    nutrition_data = nutrition_response.json()

    for nutrient in desired_nutrition:
        if nutrient in nutrition_data:
                value = nutrition_data[nutrient]
                print(f"Recipe ID: {recipe_id}, {nutrient.capitalize()}: {value}")
        else:
                print(f"{nutrient.capitalize()} not found for Recipe ID: {recipe_id}")


    








