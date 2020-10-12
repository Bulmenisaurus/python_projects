import webbrowser
import httplib2
from time import sleep
from random import choice
h = httplib2.Http()

baseurl = input("What is the baseurl of this site? Such as `https://en.wikipedia.org?\n")
# Validate site:
try:
    resp = h.request(baseurl, 'HEAD')
except:
    print("This program encountered an error reaching", baseurl)
    quit()


pages = []
print("You will be selecting which pages to viewbot now. Type 'end' to stop your selection")
while (page := input('What pages would you like to view?\n'+baseurl)) != 'end':
    pages.append(page)

print("Your selected pages are:", pages)
for x in range(int(input('How many times would you like to repeat and wait?\n'))):
    for x in range(int(input('How many pages should be opened per repetition?\n'))):
        url = baseurl+choice(pages)
        webbrowser.open(url, new=0, autoraise=True)
    sleep(int(input('How long to wait before repetition?\n')))
