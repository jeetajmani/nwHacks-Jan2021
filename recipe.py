import json


def recipe_find(ingredients):
    with open("recipebook.json", encoding="utf8") as read_file:
        data = json.load(read_file)

    recipes = data["recipes"]

    matches = []

    for x in recipes:
        c = all(i in ingredients for i in x["ingredients"])
        if c is True:
            matches.append(x)

    return matches


def thumbnail(url):
   str = "https://i.ytimg.com/vi/___/maxresdefault.jpg"

   newStr = str.replace("___", url[30:])

   return newStr


def reverse_lookup(name):
    with open("recipebook.json", encoding="utf8") as read_file:
        data = json.load(read_file)

    recipes = data["recipes"]

    for x in recipes:
        if x["name"] == name:
            return x

