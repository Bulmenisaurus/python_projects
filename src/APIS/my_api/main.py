import urllib.parse
from typing import *

url = 'https://a.com/asd?length=2&isAscii=false'
parsed_url = urllib.parse.urlparse(url)
parsed_url_query = urllib.parse.parse_qs(parsed_url.query)
#parsed_url_query = {x: x[0]}

QueryArgs = List[Tuple[str, List]]


def response_to_query(query:  Dict[str, List[str]]) -> dict:
    query_args: QueryArgs = list(query.items())

    a = filter_using_query([{"length": "2", "isAscii": "false", "emoji": "Ω"}], **query)
    print(list(a))


def filter_using_query(data, **query):
    for emoticon in data:
        if emoticon.items() <= query.items():
            yield emoticon

response_to_query(parsed_url_query)
