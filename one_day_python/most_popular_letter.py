import urllib.parse              # url encode request (just in case)
import requests                  # get html
import re                        # for some reason soup cant see some elements????

"""
Sources used: 
https://www.urlencoder.io/python/ for url encoding
"""

header = {'Accept': '*/*', 'Connection': 'keep-alive',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko)'
                        ' Chrome/70.0.3538.110 Safari/537.36', 'Accept-Language': 'en-US;q=0.5,en;q=0.3',
          'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1'}




def collect_data(letters: str) -> dict:
    all_data = {}
    for search in letters:
        goog_url = "https://www.google.com/search?q="+urllib.parse.quote(search)
        html = requests.get(goog_url, headers=header).text

        regex = r"\<div id=\"result-stats\"(.*?)\<"
        i = repr(re.search(regex, html))
        assert i is not None
        #print(i)
        try:
            all_data[search] = i[i.index("About ")+6:i.index(' re')].strip()
            print(f"{goog_url} = {all_data[search]}")
        except ValueError as err:
            print(f"An error occured on character {search}, url {goog_url}")
            print("Raw error:")
            print(err)
            continue

    return all_data


re_sults = collect_data(input("Type "))

print(re_sults)
