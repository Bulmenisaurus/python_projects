from bs4 import BeautifulSoup, element

myXml = '''<?xml version="1.0" encoding="UTF-8"?>
<code>
    <print end=" ">Hello</print>
    <print>world!</print>
    <if a="0==0"><print>hi!</print></if>
    <print>this should be seperate</print>
</code>'''

def handle_single_tag(tag: element.Tag):
    if tag.name == 'print':
        print(tag.text)


html = BeautifulSoup(myXml, 'xml')
for tag in html.code.children:
    if type(tag) == element.Tag:
        handle_single_tag(tag)