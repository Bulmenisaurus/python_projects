from datetime import date      # for random color each day
import random                  # random color
import requests                # getting html from sites
from bs4 import BeautifulSoup  # parsing that html
import webbrowser              # opening tab
import urllib.parse            # for &text= in font
from PIL import Image          # creating favicon


def day_clr():
    random.seed(str(date.today()))  # unique color each day
    print("Random color generated....")
    return "#%06x" % random.randint(0, 0xFFFFFF)


def day_quote():
    print("Getting quote HTML")
    html = requests.get("http://www.quotationspage.com/qotd.html").text
    soup = BeautifulSoup(html, "html.parser")
    quote = soup.select("dt a")[0].text
    print("Extracted quote...")
    return quote


def day_word():
    print("Getting word of the day HTML")
    html = requests.get("http://www.wordthink.com/").text
    soup = BeautifulSoup(html, "html.parser")
    word = soup.select("h2.title a")[0].text.capitalize()

    def_ = soup.select("div p")[0].text

    print("Word data collected....")
    return word, def_


img = Image.new("RGB", (16, 16), day_clr())
img.save("favicon.png")
print("Favicon generated...")

of_the_day = {
    '{setting1}': day_clr(),
    '{setting2}': urllib.parse.quote(''.join(set(day_word()[0]))),
    '{setting3}': 'Of the day!',
    '{content1}': day_word()[0],
    '{content2}': day_word()[1].replace("\n", ''),
    '{content3}': day_quote(),
    '{content4}': date.today().strftime("%B %d, %Y"),
}
print("Results compiled")

with open("of the day template.html", "r") as html_template:
    print("Opening template.")
    day_html = html_template.read()
    for x in of_the_day:
        day_html = day_html.replace(x, of_the_day[x])
    print("Template finished.")

with open("main_of the day.html", "w") as main_html:
    main_html.write(day_html)
    print("Wrote to file")

print("Opening tab.")
webbrowser.open_new("file:///Users/meow/programming/PycharmProjects/Python/major_projects/"
                    "of_the_day/main_of%20the%20day.html")
print("Done")



