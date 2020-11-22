import requests
import json
import random


def joke_api():
    """
    Thanks to https://sv443.net/jokeapi/v2/ for their clear documentation! :)

    :return: the completed joke
    """
    joke_url = "https://sv443.net/jokeapi/v2/joke/" \
               "Any?blacklistFlags=nsfw,religious,political,racist,sexist&type=single"
    json_data = json.loads(requests.get(joke_url).text)
    print(json_data)
    return json_data['joke']


def jokes():
    """
    I forgot the URL lol......

    :return: the str joke
    """
    joke_url = random.choice(
        [
            "https://official-joke-api.appspot.com/jokes/random",
            "https://official-joke-api.appspot.com/jokes/programming/random",
            "https://official-joke-api.appspot.com/jokes/knock-knock/random",
            "https://official-joke-api.appspot.com/jokes/knock-knock/general"
        ]
    )

    json_data = json.loads(requests.get(joke_url).text)
    return json_data['setup'] + '\n' + json_data['punchline']


joke_choice = random.choice([joke_api, jokes])

print(joke_choice())

