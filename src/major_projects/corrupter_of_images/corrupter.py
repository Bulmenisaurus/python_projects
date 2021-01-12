from shutil import copy
from os import rename, remove
import glob
import string
from random import shuffle, choice
import sys
from PIL import Image

print("Welcome to corruptor! This project doesnt corrupt the original image,\n"
      "but it copies the file into the corrupted folder for safekeeping. Let's start!")


filename = "/Users/meow/Downloads/PogCorn.png"

#  filename = input("What image would you like to corrupt?\n")

newdirectory = "/Users/meow/programming/PycharmProjects/Python/major_projects/corrupter_of_images/corrupted/"
newfile = "corrupted"+str(len(glob.glob('corrupted/*')))+".txt"

copy(filename, newdirectory+newfile)

with open("corrupted/"+newfile, "rb") as img:
    img = img.read()
    replace_chars = list(string.ascii_letters)
    shuffle(replace_chars)
    replace_chars = ''.join(replace_chars).encode()
    for x in replace_chars:
        x = x.to_bytes(1, sys.byteorder)
        if x in img:
            img = img.replace(x, choice(replace_chars).to_bytes(1, sys.byteorder))
            break

with open("corrupted/"+newfile, "wb") as img_w:
    img_w.write(img)

rename("corrupted/"+newfile, "corrupted/"+newfile.split('.')[0]+'.png')
image = Image.open("corrupted/"+newfile)
image.show()

