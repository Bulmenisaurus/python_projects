import requests
response = requests.get("http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
data = response.json()

MostPopularTwoLetterCombos = {}
for x in data:
    for i in range(len(x)-1):
        