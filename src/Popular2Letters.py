import requests
from PIL import Image, ImageDraw
import string
# response = requests.get("http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
# data = response.json()


def open_dict(choice_input):
    if choice_input == "s":
        response = requests.get("http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
        open_dict_return = response.json()
    else:
        with open("python_data/Dictionary.txt", 'r') as english:
            open_dict_return = english.readlines()
            for x in range(len(open_dict_return)-1):  # last line is empty
                open_dict_return[x] = open_dict_return[x].strip("\n")
    return open_dict_return


def find_letters(find_input):
    find_letters_dict = {}
    for x in find_input:
        if len(x) >= 3:  # words have to be longer or equal to 3 letters
            for i in range(len(x) - 1):  # goes through each combination
                if x[i:i + 2] in find_letters_dict:
                    find_letters_dict[x[i:i + 2]] += 1
                else:
                    find_letters_dict[x[i:i + 2]] = 1
    return find_letters_dict


def sort_letters(sort_input):
    sorted_input = {k: v for k, v in sorted(sort_input.items(), key=lambda item: item[1])}
    sorted_input = dict(zip([x for x in sorted_input.keys()][::-1], [x for x in sorted_input.values()][::-1]))
    return sorted_input


def top_letters(top_input, length_of_sample):
    print("Here are the 10 most common word combos:")
    counter = 0
    for key, value in top_input.items():
        if counter == 10:
            break
        percentage = (value / length_of_sample) * 100
        counter += 1
        print(f"{key} occurred in {percentage}% of all the words.")


choice = input("Which dictionary would you like to use? (small/big)\n").lower()[0]
data = open_dict(choice[0].lower())
sorted_data = sort_letters(find_letters(data))
print(f"Length of our data so far is {len(sorted_data)}.")
top_letters(sorted_data, len(data))

###################################
###################################
# graphs all the points on an image

main_img = Image.new("LA", (28, 28), "#FFF")  # 8-bit black/white with alpha
draw = ImageDraw.Draw(main_img)
count = 0
for j in sorted_data.keys():
    try:
        x_pos = string.ascii_lowercase.index(j[0]) + 1
        y_pos = string.ascii_lowercase.index(j[1]) + 1
        opacity = sorted_data[j] * (255 / max(sorted_data.values()))  # more common combinations are darker
        draw.point((x_pos, y_pos), fill=(000, round(opacity)))  # draw da point
    except ValueError:
        idgaf_about_this_bug = True
    count += 1
draw.line((0, 0, 0, 27), fill="#000")
draw.line((0, 0, 27, 0), fill="#000")
draw.line((27, 0, 27, 27), fill="#000")
draw.line((27, 27, 0, 27), fill="#000")
main_img.show()
