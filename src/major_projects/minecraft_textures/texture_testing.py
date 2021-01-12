import os.path          # for file validation
from os import listdir  # all files in directory
from PIL import Image   # brunt of the program, for drawing, displaying, and saving images
from math import sqrt   # sort by darkness
import random           # random file


def choose_path() -> tuple:
    path1_ = '/Users/meow/Downloads/Vanilla_Resource_Pack_1.16.20/textures/blocks/%s.png' % input('First image? \
(This is the image the colors will be taken from)\n')
    validate_path_1 = os.path.isfile(path1_)
    if not validate_path_1:
        print(f'{path1_} is an invalid path. Please try again!')
        quit()
    path2_ = '/Users/meow/Downloads/Vanilla_Resource_Pack_1.16.20/textures/blocks/%s.png' % input('Second image? \
(This is the image the shape will be taken from)\n')
    validate_path_2 = os.path.isfile(path2_)
    if not validate_path_2:
        print(f'{path2_} is an invalid path. Please try again later!')
        quit()
    return path1_, path2_


def random_path() -> list:
    files = random.choices(listdir("/Users/meow/Downloads/Vanilla_Resource_Pack_1.16.20/textures/blocks/"), k=2)
    print(' + '.join(files))
    files = ["/Users/meow/Downloads/Vanilla_Resource_Pack_1.16.20/textures/blocks/"+k for k in files]
    return files

######################################


path1, path2 = random_path()


#####################################

img_1 = Image.open(path1, 'r').convert('RGB')  # open minecraft texture in rgb mode
img_2 = Image.open(path2, 'r').convert('RGB')
img_1_clrs, img_2_clrs = {}, {}

# sort_by = input('Sort by darkness? (recommended)\n')
sort_by = 'True'

if not eval(sort_by):
    pix_val_1 = list(img_1.getdata())
    for clr in pix_val_1:
        if clr in img_1_clrs:
            img_1_clrs[clr] += 1
        elif (len(clr) == 4 and clr[3] != 0) or len(clr) == 3:
            img_1_clrs[clr] = 1

    pix_val_2 = list(img_2.getdata())
    for clr in pix_val_2:
        if clr in img_2_clrs:
            img_2_clrs[clr] += 1
        elif (len(clr) == 4 and clr[3] != 0) or len(clr) == 3:
            img_2_clrs[clr] = 1
    img_1_clrs = list({k: v for k, v in sorted(img_1_clrs.items(), key=lambda item: item[1], reverse=True)}.keys())
    img_2_clrs = list({k: v for k, v in sorted(img_2_clrs.items(), key=lambda item: item[1], reverse=True)}.keys())
else:
    def lum(r, g, b):
        return sqrt(.241 * r + .691 * g + .068 * b)

    pix_val_2 = list(img_2.getdata())
    pix_val_2 = set(pix_val_2)
    img_2_clrs = sorted(pix_val_2, key=lambda rgb: lum(*rgb))

    pix_val_1 = list(img_1.getdata())
    pix_val_1 = set(pix_val_1)
    img_1_clrs = sorted(pix_val_1, key=lambda rgb: lum(*rgb))
# set pixels of img_2 to img_1's colors

while len(img_1_clrs) < len(img_2_clrs):
    img_1_clrs.append(img_1_clrs[-1])
if len(img_1_clrs) > len(img_2_clrs):
    del img_1_clrs[len(img_2_clrs):]

# print(f"{img_1_clrs=}")
# print(f"{img_2_clrs=}")

clrs_filter = dict(zip(img_2_clrs, img_1_clrs))  # "filter", where a pixel passed in from img_2 will be img_1's color

px = img_2.load()
new_img = Image.new(mode='RGB', size=(16, 16))

for x in range(16):
    for y in range(16):
        px_clr = px[x, y]
        if px_clr not in clrs_filter:
            new_px_clr = (0, 0, 0, 0)  # transparent
        else:
            new_px_clr = clrs_filter[px_clr]
        new_img.putpixel((x, y), new_px_clr)
new_img.show()

input('Would you like to save this file? (Of not, do NOT continue)\n')
new_img.save(f"generated_images/{os.path.basename(path1).split('.')[-2]}+{os.path.basename(path2).split('.')[-2]}.png")
