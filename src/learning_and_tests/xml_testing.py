from bs4 import BeautifulSoup, element

myXml = '''<?xml version="1.0" encoding="UTF-8"?>
<code>
    <print end=" "><i>i</i></print>
    <print>world!</print>
    <if a="0==0"><print>hi!</print></if>
    <print>this should be seperate</print>
</code>'''

def handle_single_tag(tag: element.Tag):
    print(type(tag))
    print(tag)
    if tag.name == 'print':
        pass #print(tag.text, type(tag.text))


soup = BeautifulSoup(myXml, 'xml')
code: element.Tag = soup.code
tags = code.find_all(recursive=False)
print(type(tags[0].contents[0]))
print(tags[0].contents)