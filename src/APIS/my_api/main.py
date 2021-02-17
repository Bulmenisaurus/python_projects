import urllib.parse

url = 'https://a.com/asd?length=2&isAscii=false'
parsed_url = urllib.parse.urlparse(url)
parsed_url_query = urllib.parse.parse_qs(parsed_url.query)

print(f"{parsed_url_query=}")

def response_to_query(query: dict) -> dict:
    pass