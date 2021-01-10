import json


# find all possible recipes that can be made with the current ingredients
def recipe_find(ingredients):

    # store the recipes from the json file as a list
    with open("recipebook.json", encoding="utf8") as read_file:
        data = json.load(read_file)

    recipes = data["recipes"]

    matches = []

    # eliminate human error
    ingredients = list(map(str.lower, ingredients))
    ingredients = list(map(str.strip, ingredients))

    count = 0

    # add a recipe to matches if the user has the correct ingredients
    for x in recipes:
        count = len(x["ingredients"])
        x["ingredients"] = list(map(str.lower, x["ingredients"]))
        c = all(i in ingredients for i in x["ingredients"])
        if c is True:
            matches.append([x,0])
        else:
            # prioritize recipes in ascending order based on number of missing ingredients
            for y in x["ingredients"]:
                if y in ingredients:
                    count -= 1
            matches.append([x, count])

    matches.sort(key=lambda z: z[1])
    matches = [q for q in matches if q[1] < 4]
    return matches[:3]


# find the YouTube thumbnail based on the link of the video
def thumbnail(url):
   str = "https://img.youtube.com/vi/___/0.jpg"

   newStr = str.replace("___", url[30:])

   return newStr


# find the information of a recipe based on the name
def reverse_lookup(name):
    with open("recipebook.json", encoding="utf8") as read_file:
        data = json.load(read_file)

    recipes = data["recipes"]

    for x in recipes:
        if x["name"] == name:
            return x