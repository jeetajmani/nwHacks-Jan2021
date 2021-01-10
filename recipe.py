import json


def recipe_find(ingredients):
    with open("recipebook.json", "r") as read_file:
        data = json.load(read_file)

    recipes = data["recipes"]

    matches = []

    for x in recipes:
        c = all(i in ingredients for i in x["ingredients"])
        if c is True:
            matches.append(x)

    return matches


ing = ['Cooking Oil', 'Egg', 'Jasmine Rice', 'Soy Sauce', 'Salt', 'Green Onion']

recipes = recipe_find(ing)

print(recipes)
