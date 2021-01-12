import requests
import json


def get_recipe(ingredients=(), query: str = '') -> None:
    base_url = "http://www.recipepuppy.com/api/?"  # base url
    base_url += 'i='+','.join(ingredients)         # adds ingredients in url format `i=cheese, garlic,`
    base_url += '&q='+query                        # adds query in format `&q='mac and cheese'`

    print("\n\n\n\n", base_url, "\n\n\n\n\n")
    recipe_json = json.loads(requests.get(base_url).text)

    format_results(recipe_json['results'])

    while True:
        page = input("What page# would you like to view?\n")

        print(base_url)
        recipe_json = json.loads(requests.get(base_url + '&p=' + page).text)
        print(json.dumps(recipe_json, indent=4))


def format_results(results: list) -> None:
    for index, result in enumerate(results):
        formatted = "{}\nIngredients: {}\nlink: {}\n\n\n".format(result['title'], result['ingredients'], result['href'])
        print(str(index)+")\n"+"-"*50)
        print(formatted)


get_recipe(
    input("What ingredients do you have available? Enter a comma-separated list!\n")
    .replace(' ', '')
    .split(','),

    input("Enter a specific search query, such as 'omelet' in here! [Don't type anything if nothing]\n")
    .strip()
    .lower()

)
