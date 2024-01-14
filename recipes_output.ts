import { title } from "process"

interface nutritiontype { Calories: string, Fat: string, Carbohydrates: string, Sodium: string, Protein: string, Fiber: string }
interface datatype { title: string, image: string, usedIngredients: string[], missedIngredients: string[], nutrition: nutritiontype, instructions: string[] }

const data: datatype[] = [{
    "title": "Curry Chicken Salad",
    "image": "https://spoonacular.com/recipeImages/650378-312x231.jpg",
    "usedIngredients": [
        "carrot",
        "cucumber",
        "grapes",
        "salad greens"
    ],
    "missedIngredients": [
        "chicken",
        "celery",
        "madras curry powder",
        "mayonnaise",
        "turmeric powder"
    ],
    "nutrition": {
        "Calories": "682.54 kcal",
        "Fat": "52.87 g",
        "Carbohydrates": "16.53 g",
        "Sodium": "1018.86 mg",
        "Protein": "34.64 g",
        "Fiber": "2.91 g"
    },
    "instructions": [
        "Step 1: Strain the water from the cans of chicken and place the chicken in large mixing bowl.",
        "Step 2: Add mayonnaise. You can use more or less based on how moist you like your chicken salad.Season with salt and pepper to taste, go easy on the seasoning at this point because the main seasoning will occur at the end when you add the spices. Drop in the diced celery, carrot, cucumber and grapes and mix well. Once all the ingredients have been combined, add additional mayonnaise if you prefer a wetter consistency to the salad.Once the consistency is right, add in curry powder and turmeric powder. These are they key ingredients, so make sure you are using high quality spices. Start with a small amount of each spice and gradually add to taste - the measurements here are just recommendations, you should taste test as you go along. If possible, pop your mixing bowl into the fridge for an hour to let the flavors marry.",
        "Step 3: Serve of the Curry Chicken Salad on top of salad greens, no dressing necessary."
    ]
},
{
    "title": "Mediterranean Spinach Artichoke Dip",
    "image": "https://spoonacular.com/recipeImages/651437-312x231.jpg",
    "usedIngredients": [
        "artichoke hearts",
        "neufchatel cheese",
        "monterey jack cheese",
        "parmesan cheese",
        "shallots"
    ],
    "missedIngredients": [
        "spinach",
        "nonfat greek yogurt",
        "sun tomatoes",
        "garlic cloves",
        "thyme",
        "paprika",
        "kosher salt and pepper"
    ],
    "nutrition": {
        "Calories": "117.7 kcal",
        "Fat": "6.89 g",
        "Carbohydrates": "7.57 g",
        "Sodium": "456.19 mg",
        "Protein": "7.41 g",
        "Fiber": "2.25 g"
    },
    "instructions": [
        "Step 1: Preheat oven to 350 degrees.",
        "Step 2: In a large skillet, heat the oil from the sun dried tomatoes.",
        "Step 3: Add shallots and cook until translucent.",
        "Step 4: Add garlic and cook for an additional minute.",
        "Step 5: Add sun dried tomatoes, artichoke hearts, and dried thyme. Stir and cook for 2-3 minutes before adding the spinach. Cook for an additional few minutes and then transfer all items into a large bowl.",
        "Step 6: Add Neufchatel, Greek Yogurt, Monterey Jack Cheese and paprika to the spinach mixture. Season with salt and pepper.",
        "Step 7: Combine well. Lightly cover ramekins or other baking dishes with cooking spray. Spoon spinach mixture into the dishes and sprinkle the tops with Parmesan Cheese.",
        "Step 8: Bake for 20-25 minutes and then turn the broiler on. Broil the tops until they are golden brown.",
        "Step 9: Serve with chips, bread slices, crackers, or vegetable sticks."
    ]
},
{
    "title": "Spinach Salad with Strawberry Vinaigrette",
    "image": "https://spoonacular.com/recipeImages/661340-312x231.jpg",
    "usedIngredients": [
        "chicken",
        "feta cheese",
        "shallot",
        "strawberries"
    ],
    "missedIngredients": [
        "almonds",
        "balsamic vinegar",
        "dijon mustard",
        "thyme",
        "ground pepper",
        "spinach leaves",
        "water"
    ],
    "nutrition": {
        "Calories": "321.81 kcal",
        "Fat": "12.73 g",
        "Carbohydrates": "29.95 g",
        "Sodium": "341.17 mg",
        "Protein": "22.03 g",
        "Fiber": "6.47 g"
    },
    "instructions": [
        "Step 1: Place everything on a plate!  :)"
    ]
},
{
    "title": "Warm Goat Cheese Salad",
    "image": "https://spoonacular.com/recipeImages/664961-312x231.jpg",
    "usedIngredients": [
        "rounds goat cheese",
        "grapes",
        "salad greens",
        "shallot"
    ],
    "missedIngredients": [
        "some bread crumbs",
        "lemon juice",
        "olive oil",
        "pepper",
        "salt and pepper",
        "walnut oil",
        "walnuts"
    ],
    "nutrition": {
        "Calories": "481.22 kcal",
        "Fat": "41.94 g",
        "Carbohydrates": "15.68 g",
        "Sodium": "461.29 mg",
        "Protein": "13.72 g",
        "Fiber": "2.04 g"
    },
    "instructions": [
        "Step 1: Whisk together 3 tablespoons of walnut oil with lemon juice, minced shallot, salt and pepper to make a vinaigrette. Coat each goat cheese round with walnut oil and then the bread crumbs, patting the crumbs to adhere.",
        "Step 2: Combine the greens and the walnuts in a large bowl.",
        "Step 3: Add in enough of the vinaigrette and toss well. Adjust the seasoning and divide among two serving plates.",
        "Step 4: Heat a nonstick skillet over medium heat.",
        "Step 5: Add in olive oil. When the oil is hot, add the goat cheese rounds. Cook until nicely browned, about 30 seconds. Turn and cook the other side. Do not allow it to burn or melt.",
        "Step 6: Transfer the goat cheese to the plates, placing 2 or 3 atop each salad.",
        "Step 7: Sprinkle the cheese with freshly ground pepper and garnish with grape wedges."
    ]
},
{
    "title": "Citrus and Asparagus Salad",
    "image": "https://spoonacular.com/recipeImages/639510-312x231.jpg",
    "usedIngredients": [
        "bundle of asparagus",
        "t.finely shallot",
        "spring greens",
        "feta cheese"
    ],
    "missedIngredients": [
        "grapefruit",
        "naval oranges",
        "lemon juice",
        "mint",
        "olive oil",
        "salt",
        "pepper",
        "quinoa",
        "pepitas"
    ],
    "nutrition": {
        "Calories": "451.4 kcal",
        "Fat": "27.73 g",
        "Carbohydrates": "45.28 g",
        "Sodium": "451.34 mg",
        "Protein": "9.5 g",
        "Fiber": "6.92 g"
    },
    "instructions": [
        "Step 1: Using a sharp knife, cut the ends off  one of the grapefruit.",
        "Step 2: Cut away the peel and white pith, following the natural curve of the fruit with your knife. Then cut the peeled grapefruit lengthwise into quarters, then slice into 1/4-inch slices. Repeat this process with one of the oranges. Set the cut fruit aside in a bowl.",
        "Step 3: With the remaining grapefruit and orange, squeeze 2 T. juice from each fruit.",
        "Step 4: Combine grapefruit and orange juice with the lemon juice, shallot, mint, olive oil, salt and a few grindings of fresh black pepper.",
        "Step 5: Whisk to emulsify, set aside.",
        "Step 6: Meanwhile, in a saucepan fitted with a steamer basket, bring a couple of inches of water to a boil, add the asparagus and steam for about 5 minutes, until just becoming tender. Immediately plunge the asparagus into a bowl of ice water to stop the cooking.",
        "Step 7: Drain and pat briefly with paper towel. In a medium bowl, toss asparagus with 1 1/2 T. of the dressing. In another bowl, toss quinoa with 1/4 c. of the dressing.",
        "Step 8: To assemble the salad: toss the salad greens with half of the remaining dressing. Heap the quinoa in the center of a large bowl, layer the asparagus and citrus over the salad.",
        "Step 9: Sprinkle with the feta and pepitas and drizzle with the remaining dressing."
    ]
}
]
export default data