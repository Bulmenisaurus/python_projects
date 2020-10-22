import requests
from bs4 import BeautifulSoup


# this site #
request = requests.get("https://htmlcolorcodes.com/color-names/")
html_ = request.text

soup = BeautifulSoup(html_, "html.parser")

colors = soup.select("tr.color td.color-name h4")
print(colors)
colors = [x.text for x in colors]
print(len(colors))

# wikipedia #

request = requests.get("https://en.wikipedia.org/wiki/List_of_colors_(compact)")
html_ = request.text

soup = BeautifulSoup(html_, "html.parser")

colors_2 = soup.select("div p")[1:]
colors_2 = colors_2[::-2]
#print(colors)

colors_2 = [x.text if ' ' not in x.text else '' for x in colors_2]
print(len(set(colors_2)))