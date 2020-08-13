import requests
from PIL import Image, ImageDraw
import string
response = requests.get("http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
data = response.json()

TwoLetters = {}
for x in data:
    for i in range(len(x)-1):
        if x[i:i+2] in TwoLetters:
            TwoLetters[x[i:i+2]] += 1
        else:
            TwoLetters[x[i:i + 2]] = 1
SortedTwoLetters = {k: v for k, v in sorted(TwoLetters.items(), key=lambda item: item[1])}
SortedTwoLetters = dict(zip([x for x in SortedTwoLetters.keys()][::-1], [x for x in SortedTwoLetters.values()][::-1]))
for x in SortedTwoLetters:
    if SortedTwoLetters[x] > 0:
        print(f"{x}:  {SortedTwoLetters[x]}")


###################################
###################################
# graphs all the points on an image

main_img = Image.new("LA", (26, 26), "#FFF")  # 8-bit black/white with alpha
draw = ImageDraw.Draw(main_img)
for x in SortedTwoLetters.keys():
    x_pos = string.ascii_lowercase.index(x[0])
    y_pos = string.ascii_lowercase.index(x[1])
    draw.point((x_pos, y_pos), fill="#000")
draw.point((0, 0), fill=(000, 100))
main_img.show()
