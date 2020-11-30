import requests
import urllib.parse
import re
import json


def color_google_popularity(color: str) -> int:
    # hackerman headers 8)
    header = {'Accept': '*/*', 'Connection': 'keep-alive',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko)'
                            ' Chrome/70.0.3538.110 Safari/537.36', 'Accept-Language': 'en-US;q=0.5,en;q=0.3',
              'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1'}

    search_url = "https://www.google.com/search?q=" + urllib.parse.quote(color)  # request url
    html = requests.get(search_url, headers=header).text               # get response html
    results_re = re.compile(r'\"result-stats\">(.*?)<')              # compile regex bc we da cool ones
    result = results_re.search(html).group(1)                        # find right pattern, and .group(1) is a lifesaver

    final = result.lstrip('About').rstrip('results').replace(',', '')  # finally format stuff

    return int(final)  # int automatically strips spaces yay


def color_colornames_api(color: str) -> str:
    color_url = "https://colornames.org/search/json/?hex=" + color.strip("#")
    json_data = requests.get(color_url).text
    color_name = json.loads(json_data)

    return color_name['name']


def color_thecolorapi(color: str) -> dict:
    color_url = "https://www.thecolorapi.com/id?hex="+color.strip('#')
    json_data = requests.get(color_url).text
    color_data = json.loads(json_data)

    data = {
        'conversions': {
            x: color_data[x]['value'] for x in [
                'rgb', 'hsv', 'hsl', 'cmyk', 'XYZ'
            ]
        },

        'name': color_data['name']['closest_named_hex']
    }

    return data





