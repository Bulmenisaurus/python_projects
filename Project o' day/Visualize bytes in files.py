import os
from collections import Counter
from PIL import Image, ImageDraw

file = input("What is the path to your file?\n")
head, tail = os.path.split(file)
print(f"Opening file\033[1m{tail}"+'\033[0m')

byte_size = os.path.getsize(file)  # tells me the size of the file in bytes
with open(file, "rb") as fi:       # reads file as bytes
    contents = list(fi.read(os.path.getsize(file)))  # convert byte type into actual bytes
print(len(contents))


################################
################################
# Graphs all the points!


def lerp(a, b, percent):
    return a + (b - a) * (percent/100)


occurrences = dict(Counter(contents))
popular_byte_count = next(iter(occurrences.values()))

count = 0
main_img = Image.new("RGB", (256, 256), "#FFF")
draw = ImageDraw.Draw(main_img)
rangenum = len(occurrences.values())-2
for x in range(len(occurrences.values())-2):

    x_pos = list(occurrences.keys())[x]
    y_pos = list(occurrences.keys())[x+1]

    value = ((occurrences[x_pos] + occurrences[y_pos])/2)/popular_byte_count * 255

    if value > 255:
        value = 255
    color = (round(lerp(0, 255, value)), 0, round(lerp(0, 255, value)))
    draw.point((x_pos, y_pos), color)  # draw da point
    count += 1

print(count)
main_img.show()
