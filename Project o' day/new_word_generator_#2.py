"""
Oopen file, extrcat
"""


with open("../Dictionary.txt", "r") as dict_:
    data_ = dict_.read().splitlines()[:1000]

valid_letters = list("abcdefghijklmnopqrstuvwxyz")
valid_letters += [i.upper() for i in valid_letters]
print(valid_letters)


print(data_)

for wrd in data_:
    for index, lttr in enumerate(wrd)



