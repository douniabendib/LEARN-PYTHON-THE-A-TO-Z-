"""
You are managing a digital recipe book where each recipe is stored 
as a dictionary. Each dictionary contains the name of the recipe 
as the key and a list of ingredients as the value. 
Your task is to perform several operations to update 
and manage the recipe book.

Create the Recipe Book:
Create a dictionary named recipe_book with the following recipes:
"Pancakes": ["flour", "milk", "eggs", "sugar"]
"Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
Access Ingredients:
Print the list of ingredients for "Pancakes".
Add a New Recipe:
Add a new recipe "Smoothie" with the ingredients 
["banana", "milk", "honey"] to the dictionary.
Modify a Recipe:
Add "blueberries" to the "Smoothie" recipe.
Print All Recipes:
Print the entire recipe_book dictionary to verify the updates.
"""
recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
}

print(recipe_book["Pancakes"])
recipe_book["Smoothie"] = ["banana", "milk", "honey"]
recipe_book["Smoothie"].append("blueberries")

print(recipe_book)
