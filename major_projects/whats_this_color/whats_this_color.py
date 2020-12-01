from bs4 import BeautifulSoup
from time import time
color_data = __import__("get_colordata")


timer_start = time()
COLOR = input("What color would you like to examine? [input as a 6-digit hexadecimal]\n")
NAME = color_data.get_color_name(COLOR)
GOOG = color_data.color_google_popularity(COLOR)


with open("whats_this_color_original.html", "r") as f:
    soup = BeautifulSoup(f, 'html.parser')


# document stuff
soup.find('title').string = COLOR + " - " + NAME
soup.find('h1').string = COLOR
soup.find('h3').string = NAME

# images
soup.find('rect')['fill'] = COLOR

# results
results = f"{GOOG} google results, python executed in {round(time() - timer_start, 3)} seconds"
results_tag = soup.find(id='results')
results_tag.string = results

# display

with open("whats_this_color_ouput.html", "w") as html_file:
    html_file.write(soup.prettify())
