import requests                 # for extracting html from sites
from bs4 import BeautifulSoup   # parsing and getting data from that htm
from random import choice       # making ai-based predictions
import matplotlib               # next two imports are for graphing
import matplotlib.pyplot as plt
from datetime import date

url = "https://weather.com/coronavirus/l/Redmond+WA?canonicalCityId=" \
      "002d6e6aaed0de430256e4a07b419e1bc47345280591027eabbf182603423f3f"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

tags = ['span.CovidCasesOverview--primaryCount--3yVlK']

extracted_data = soup.select(tags[0]) # python equivalent of js's document.querySelector
print(extracted_data[0].text, extracted_data[1].text)

log = repr(
    {
        'total_confirmed': extracted_data[0].text,
        'total_deaths': extracted_data[1].text,
        'date': str(date.today())
    }
)

print(log)

with open("python_data/covid_data", "a") as log_file:
    log_file.write(log+'\n')

# TODO: graph these values, write data to a file

plot_data = []

with open("python_data/covid_data", "r") as log_file:
    for x in log_file.read().split('\n'):
        if x == '':
            continue
        plot_data.append(eval(x)['total_confirmed'])


fig, ax = plt.subplots()
ax.plot(plot_data)


ax.set(xlabel='time (s)', ylabel='Cases',
       title='We are'+choice(['screwed!', 'not screwed.']))

ax.grid()
plt.show()
