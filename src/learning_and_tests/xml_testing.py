from bs4 import BeautifulSoup, element

myXml = '''<?xml version="1.0" encoding="UTF-8"?>
<code>
    <print end=" "><i>i</i></print>
    <print>world!</print>
    <if a="0==0"><print>hi!</print></if>
    <print>this should be seperate</print>
</code>'''

def handle_single_tag(tag: element.Tag):
    if tag.name == 'print':
        print(tag.text)


def does_tag_contain_other_tags(tag: element.Tag):
    return type(tag.contents[0]) == element.Tag


soup = BeautifulSoup(myXml, 'xml')
code: element.Tag = soup.code
tags = code.find_all(recursive=False)

for tag in tags:
    if does_tag_contain_other_tags(tag):
        pass
    else:
        handle_single_tag(tag)