import string
from PIL import Image, ImageColor


def _encode_letters(letters: str):
    lookup_table = {
        '': '111111111', ' ': '000000000',
        '0': '111101111', '1': '110010111',
        '2': '110010011', '3': '111011111',
        '4': '110110010', '5': '111100011',
        '6': '110111111', '7': '111010100',
        '8': '010010111', '9': '111111001',
        'A': '010101101', 'a': '000011111',
        'B': '110111111', 'b': '100111111',
        'C': '110100111', 'c': '000110110',
        'D': '110100110', 'd': '001011011',
        'E': '111110111', 'e': '000110110',
        'F': '111110100',
        'G': '110101111',
        'H': '101111101',
        'I': '111010111',
        'J': '111001011',
        'K': '101110101',
        'L': '100100111',
        'M': '111101101',
        'N': '101111101',
        'O': '111101111',
        'P': '111111100',
        'Q': '111101110',
        'R': '111110101',
        'S': '111010101',
        'T': '111010010',
        'U': '101101111',
        'V': '101101010',
        'W': '101111111',
        'X': '101010101',
        'Y': '101010010',
        'Z': '111010111',
    }
    image = []
    for x in letters:
        x = str(x)
        image.append(lookup_table[x] if x in lookup_table else lookup_table[''])

    return image


def _draw_letter(unencoded_letter, color: bool = False):
    """Draw letter initially so you can just paste it on the main image"""
    encoded_letter = _encode_letters(unencoded_letter)[0]
    letter_img = Image.new('RGB', (3, 3), (255, 255, 255))

    coordinates = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    letter_color = ImageColor.getrgb(_assign_color(unencoded_letter)) if color else (0, 0, 0)

    for pixel_num, pixel in enumerate(str(encoded_letter)):
        if int(pixel):
            Image.Image.putpixel(letter_img, coordinates[pixel_num], letter_color)
    return letter_img


def _assign_color(letter):
    """If you want colorful text and/or kinda syntax highlighting?"""
    if letter in list('0123456789'):
        return ["#919191",
                "#86939c", "#7b94a7",  "#7096b2",
                "#6597bd", "#5b99c8", "#509ad3",
                "#459cde", "#3a9de9", "#178EE9"][int(letter)]
    elif letter in string.ascii_letters:
        if letter.isupper():  # Uppercase
            return "#2A813C"
        else:
            return "#6dbb5b"
    elif letter in string.punctuation:
        return "#ff9000"
    else:
        return "#191f45"


def letter_strip(letters):
    main_img = Image.new('RGB', (len(letters)*3, 3), (255, 255, 255))
    for x_coord, x in enumerate(letters):
        main_img.paste(_draw_letter(x, color=True), (x_coord*3, 0))
    return main_img


message = input('What would you like to imagize?\n')
letter_strip(message).show()



