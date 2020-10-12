"""
fantasy_language

Description: Using advanced techniques, I can make fake words!
Skillset:

function, dictionaries, loops, modules, list slicing
"""

from time import sleep as wait, time
from random import choice, randint


def random_word_len():
    """Since I can't use random.choices(),
    I have to implement another algorithm."""
    weights = (0, .1, .6, 2.6, 5.2, 8.5, 12.2, 14.0, 14.0, 12.6, 10.1, 7.5, 5.2, 3.2, 2.0, 1.0, .6, .3, .2, .1)

    rnd = randint(0, 100)

    for i in range(20):  # since I know there are 20 possible word lengths
        if rnd < weights[i]:
            return i
        rnd -= weights[i]


def gen_new_word(approx_len):
    pref = "Re Dis Over Un Mis Out In Im Il Ir".split(' ')
    suff = "lo er ism xho dla fre ity tion ment ness".split(' ')

    gen_word = ''  # final words

    if choice(range(3)) == 1 and approx_len > 5:
        gen_word += choice(pref)
    elif approx_len == 3:
        gen_word += choice(list('AUIOYETBP'))
    else:
        gen_word += choice(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    # keys = letter, values = the next possible letters after that
    word_rules = {
        'a': 'werrrttttyuuipppsssdddfffddghjjkllllzxccvbnmmuu',
        'b': 'eerryuiooaaallv',
        'c': 'weerryuuohkkoahhhkkkll',
        'd': 'weerryuuiiooaahllv',
        'e': 'qqwrrrtttpsddfggghjklzxcvbnnnm',
        'f': 'eeryuioooaaluuan',
        'g': 'hhhhhwweeeryuuuioaahlllxvvnnnn',
        'h': 'eeeeryyyyyyyuiiioallnm',
        'i': 'weerrtyuoppassdfghjkllzzzxcvbnm',
        'j': 'eyuiioooaallv',
        'k': 'wwerryyuiioafhhllvmm',
        'l': 'eeeyyyuuuuuiooaa',
        'm': 'eeerryyuuiooaauhllv',
        'n': 'eeeyuiooaahv',
        'o': 'wwrrrrtiooopassddfghjkllzzvbbnm',
        'p': 'eerrryyuuoaahhhhhhllvv',
        'q': 'eeiiiioooa',
        'r': 'eeeyyyuuuiiioaahhhoooaah',
        's': 'eerryyuuiioaahlllnnmm',
        't': 'wweeryyuuiooahhhhlllv',
        'u': 'rraayyoalxvcnmddm',
        'v': 'eeyyuuiiooaaoollm',
        'w': 'eeaayiuoaa',
        'x': 'iieeuooyy',
        'y': 'eoaatnmio',
        'z': 'eerryuuiiooahll',
    }
    for _ in range(approx_len - len(gen_word)):  # so the prefix doesn't make the word too long
        gen_word += choice(word_rules[gen_word[-1].lower()])
    if choice(range(3)) == 1 and approx_len > 6:
        new_suff = choice(suff)
        gen_word = list(gen_word)
        gen_word[-len(new_suff):] = new_suff  # replace last x letters with suffix
        gen_word = ''.join(gen_word)  # list to string
    return gen_word


start_time = time()
print("Generating 1000 new words...")
words = []
for x in range(1000):
    lengthasaurus = random_word_len()
    if type(lengthasaurus) == int:
        words.append(gen_new_word(lengthasaurus))
    else:
        print("Error on num", x)
        print(lengthasaurus)

print("Generating took " + str(time() - start_time) + " seconds.")
print('\n'.join(sorted(words)))
