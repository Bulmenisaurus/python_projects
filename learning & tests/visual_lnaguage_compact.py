# No modules! I'm super proud of this :-)

def _fetch_letter(letter):
    """
    Fetches base-10 integer (to be converted to binary later), corresponding to each letter or number.

    """

    # TODO: Maybe add support for newlines, and other common symbols such as `.`, `,`, and ( ) + [ ]
    raw_letter = {' ': 0, '1': 407, '0': 495, '3': 479, '2': 403, '5': 483, '4': 434, '7': 468, '6': 447,
                  '9': 505, '8': 151, 'A': 173, 'C': 487, 'B': 447, 'E': 503, 'D': 422, 'G': 431, 'F': 372, 'I': 471,
                  'H': 381, 'K': 373, 'J': 470, 'M': 493, 'L': 295, 'O': 495, 'N': 381, 'Q': 494, 'P': 508, 'S': 214,
                  'R': 437, 'U': 367, 'T': 466, 'W': 383, 'V': 362, 'Y': 338, 'X': 341, 'Z': 403, 'a': 155, 'c': 54,
                  'b': 319, 'e': 54, 'd': 127, 'g': 25, 'f': 500, 'i': 130, 'h': 310, 'k': 309, 'j': 150, 'm': 319,
                  'l': 146, 'o': 27, 'n': 54, 'q': 217, 'p': 436, 's': 30, 'r': 52, 'u': 47, 't': 186, 'w': 63, 'v': 42,
                  'y': 28, 'x': 45, 'z': 51}
    raw_letter = raw_letter[letter] if letter in raw_letter else 511
    # Unknown characters return a full 3*3 grid since � is too detailed and □ would look like an O or a 0
    return raw_letter


def _make_letter(letter, bin_1, bin_0):
    # the 2 '.replace''s are kinda wonky but idk any other ways to replace multiple characters...
    # the rjust is to make everything 9 characters long, so it makes a perfect grid [leading zeros can't be represented]
    raw_letter = bin(_fetch_letter(letter))[2:].rjust(9, '0') \
        .replace("0", bin_0) \
        .replace("1", bin_1)

    raw_letter = [[raw_letter[:3]], [raw_letter[3:6]], [raw_letter[6:9]]]  # splits each letter into 3 rows
    return raw_letter


def _chain_letters(message, bin_1, bin_0):
    """
    Simple function to make a list of letters from an input
    """
    return [_make_letter(_, bin_1, bin_0) for _ in message]


def _render_line(line, raw, sep):
    """
    Renders only one row of letters at a time
    """
    if raw:
        print(line)
    else:
        flattened_line = []
        for sublist in line:
            for item in sublist:
                flattened_line.append(item)  # combats the nested mess of lists I made
        print(sep.join(flattened_line))


def render_letters(message, raw=False, bin_1='W', bin_0=' ',  sep=' '):
    all_letters = _chain_letters(message, bin_1, bin_0)
    lines = [k[0] for k in all_letters], [k[1] for k in all_letters], [k[-1] for k in all_letters]  # also wonky :/

    for line in lines:
        _render_line(line, raw, sep)


# This is where the 'UI' starts. The main code is over.

print("Welcome to this project, where you can write ANY text! And nobody will care about the font! ;)")
print("First, you'll have some basic options.")
print("Don't type ANYTHNG and just press enter if you want the advanced options.\n"+"—"*100)

while (x := input('What would you like to print?\n')) != '':
    render_letters(x)

centered = "Advanced options start".center(100)
print("—"*100+"\n"+centered+"\n"+"—"*100)
while True:
    render_letters(
        message=input("What is your message?\n"),
        raw=not eval(input('Should python lists be displayed [False], or pretty strings? [True]\n')),
        bin_1=input('What should the value of 1 (the filling character) be? [Usually `W`]\n'),
        bin_0=input('What should the value of 0 (the empty character) be in the letters? [Usually just a space]\n'),
        sep=input("How should the letters be seperated? [Usually a space]\n")
    )
