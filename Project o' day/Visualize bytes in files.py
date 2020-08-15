import os
from collections import Counter
from PIL import Image, ImageDraw
from math import sqrt

file = "Dictionary.txt"
head, tail = os.path.split(file)
print(f"Opening file \033[1m{tail}"+'\033[0m')

byte_size = os.path.getsize(file)  # tells me the size of the file in bytes
with open(file, "rb") as fi:       # reads file as bytes
    contents = list(fi.read(os.path.getsize(file)))  # convert byte type into actual bytes
print(len(contents))


################################
################################
# Graphs all the points!

pair_counts = {}
def lerp(a, b, percent):  # x percent of the way between to numbers. Very useful!
    return a + (b - a) * (percent/100)


count = 0

dimensions = input("Would you like your graph to be 1d or 2d?\n")

if dimensions[0] == "2":
    main_img = Image.new("RGB", (256, 256), "#FFF")
    draw = ImageDraw.Draw(main_img)
    rangenum = len(contents)-1
    for x in range(len(contents)-1):
        x_pos = contents[x]  # x position of the dot is x'th number
        y_pos = contents[x+1]
        if (x_pos, y_pos) in pair_counts:
            pair_counts[(x_pos, y_pos)] += 1  # if (x, y) already in dict, change their count by 1
        else:
            pair_counts[(x_pos, y_pos)] = 1  # otherwise, add them to the dict with a count of 1
    for j in pair_counts:
        value = round(min(pair_counts[j], 20000) / 20000 * 255)
        color = (value, 30, value)
        draw.point((j[0], j[1]), color)

print(count)
main_img.show()
