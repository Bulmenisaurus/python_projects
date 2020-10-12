from bs4 import BeautifulSoup           # for parsing html and getting useful data
import requests                         # for actually receiving that html
from collections import namedtuple      # Organize data so you can easily access and read it
import unicodedata                      # Removing all the \x0a's and other stuff from beautifulSoup's mess
from time import sleep as chill, time   # So that all that informatino doesn't overwhelm rigth away

startTime = time()
# I have no idea why I don't need to explicitly follow the redirect, but I'll take it
page = requests.get('https://en.wikipedia.org/wiki/Special:Random')
soup = BeautifulSoup(page.content, 'html.parser')

print(f"Took {(time()-startTime)} secs to process request & get html")
process_time = time()


def list_toString(the_list: list, brackets='[]'):
    return_thing = brackets[0] if brackets else ''
    for x in the_list:
        return_thing += "\""+x+"\", "  # json proved that double quotes are superior
    return_thing = list(return_thing)
    del return_thing[-1]  # deletes comma
    return_thing[-1] = brackets[1] if brackets else ''  # so u have the option to have ["a" instead of ["a"]
    return ''.join(return_thing)


def collect_data_single(raw_soup):
    Data = namedtuple('data', ['html_title',
                               'document_title',
                               'letter_data',
                               'word_data',
                               'links',
                               'article_len'])

    html_title_ = raw_soup.title.text
    document_title_ = raw_soup.select('#firstHeading')[0]

    article = unicodedata.normalize('NFKD', raw_soup.select('#bodyContent')[0].text)
    letters_data = {}
    for _ in list(article):
        _ = _.replace('\n', '\\n')
        if _ in letters_data:
            letters_data[_] += 1
        else:
            letters_data[_] = 1
    letters_data_ = sorted(letters_data.items(), key=lambda x: x[1], reverse=True)

    words_data = {}
    for _ in list(article.split(' ')):
        _ = _.replace('\n', '\\n')
        if _ in words_data:
            words_data[_] += 1
        else:
            words_data[_] = 1
    words_data_ = sorted(words_data.items(), key=lambda x: x[1], reverse=True)

    article_len_ = len(article)

    links = []
    for link in soup.find_all('a'):
        if link.get('href'):
            links.append(link.get('href'))
    return Data(
        html_title_,
        document_title_.text,
        letters_data_,
        words_data_,
        links,
        article_len_
    )


def organize_horrific_data(horrific_data):
    beautified_data = ['']*10

    beautified_data[0] = f'\33[1m\33[4m{horrific_data.html_title}\33[0m'            # pretty colors oooooo
    beautified_data[2] = f'\33[1m\33[32m {horrific_data.document_title}\33[0m:'
    beautified_data[3] = f'\033[90mArticle {horrific_data.article_len} characters long'
    beautified_data[4] = "Note that this does include images, the title, and references.\33[0m"
    if len(horrific_data.letter_data) > 10:
        letters_1 = list_toString([x[0] for x in horrific_data.letter_data[:5]], '[ ')
        letters_2 = list_toString([x[0] for x in horrific_data.letter_data[-5:]], ' ]')
        letters_beautified = letters_1 + ' ... ' + letters_2
    else:
        letters_beautified = list_toString(horrific_data.letter_data)
    beautified_data[6] = f"Top letters: {letters_beautified}"

    if len(horrific_data.word_data) > 10:  # "preview" the list, as to not take up the whole screen
        words_1 = list_toString([x[0] for x in horrific_data.word_data[:5]], '[ ')
        words_2 = list_toString([x[0] for x in horrific_data.word_data[-5:]], ' ]')
        words_beautified = words_1 + ' ... ' + words_2
    else:
        words_beautified = list_toString(horrific_data.letter_data)
    beautified_data[7] = f"Top words: {words_beautified}"

    if len(horrific_data.links) > 10:
        beautified_data[9] = list_toString(horrific_data.links[:9], '[ ') + ' ... ]'
    else:
        beautified_data[8] = list_toString(horrific_data.links)

    return '\n'.join(beautified_data)  # You can adjust line-spacing really easy, or even compact mode!


wikiData = collect_data_single(soup)  # useful for extracting data, such as wikiData.links
wikiData_good = organize_horrific_data(wikiData)  # beautifies, cant use it for data
print(f"Took {time() - process_time} secs to extract data & bautify")

print("\n\n\n", page.url)
print()

print(wikiData_good)
chill(10)

print('\n\n')
# additional data time!
print('Would you like to view any additional data?')
print("Your options are:", ['html_title', 'document_title', 'letter_data', 'word_data', 'links', 'article_len'])
extened_data = input('')
print(['html_title', 'document_title', 'letter_data', 'word_data', 'links', 'article_len'])
print(eval('wikiData.' + extened_data))
