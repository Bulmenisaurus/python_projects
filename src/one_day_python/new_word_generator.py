from time import sleep as wait
from random import choice, randint, choices
from collections import namedtuple
import pyphen
import statistics


class Colors:
    PURPL = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    YELLO = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def gen_new_word(approx_len):
    word_weights = (0, .1, .6, 2.6, 5.2, 8.5, 12.2, 14.0, 14.0, 12.6, 10.1, 7.5, 5.2, 3.2, 2.0, 1.0, .6, .3, .2, .1)
    if approx_len == 0:
        approx_len = choices(list(range(2, 22)), weights=word_weights)[0] or approx_len
    pref = "Re Dis Over Un Mis Out In Im Il Ir".split(' ')
    suff = "lo er ism xho dla fre ity tion ment ness".split(' ')

    gen_word = ''

    if choice(range(3)) == 1 and approx_len > 5:
        gen_word += choice(pref)
    elif approx_len == 3:
        gen_word += choice(list('AUIOYE'))
    else:
        gen_word += choice(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

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
    for _ in range(approx_len-len(gen_word)):
        gen_word += choice(word_rules[gen_word[-1].lower()])
    if choice(range(3)) == 1 and approx_len > 6:
        new_suff = choice(suff)
        gen_word = list(gen_word)
        gen_word[len(new_suff):] = new_suff
        gen_word = ''.join(gen_word)
    return gen_word


def make_report(num_words):
    Report = namedtuple('Report', ['avg_score', 'med_score', 'highest_word', 'lowest_word', 'raw_data', 'alphabetized_data'])  # actual return
    word_data = {}
    for _ in range(num_words):
        dat_word = gen_new_word(0)
        if dat_word not in word_data:
            word_data[dat_word] = len(dat_word) / len(dic.inserted(dat_word).split('-'))
    the_report = Report(
        avg_score=sum(word_data.values())/len(word_data),
        med_score=statistics.median(list(word_data.values())),
        highest_word=sorted(word_data)[0],
        lowest_word=sorted(word_data)[-1],
        raw_data=word_data,
        alphabetized_data=sorted(word_data),
    )
    return the_report


dic = pyphen.Pyphen(lang='nl_NL')
while True:
    print(f"""\nWould you like to:
    {Colors.PURPL}[0]{Colors.ENDC} Generate word
    {Colors.BLUE}[1]{Colors.ENDC} Gen word with custom len
    {Colors.GREEN}[2]{Colors.ENDC} Generate x words.
    {Colors.YELLO}[3]{Colors.ENDC} Get letters per syllable
    \33[36m[4]{Colors.ENDC} Generate report
    \33[32m[5]{Colors.ENDC} Lorem Ipsum / Lorizzle Shizzle generator""")

    try:
        action = int(input())
    except ValueError:
        print(f'{Colors.RED}\033[3mNot a valid actionType{Colors.ENDC}')
        continue
    if action not in range(6):
        print(f'{Colors.RED}\033[0mNot a valid actionType[num]{Colors.ENDC}')
        continue
    print(Colors.ENDC)
    if action == 0:
        print(gen_new_word(0))

    elif action == 1:
        print(gen_new_word(int(input('How long should the word be?\n'))))

    elif action == 2:
        nums = int(input("How many words would you like to generate?\n"))
        words_l = []
        for x in range(nums):
            words_l.append(gen_new_word(0))
        print('\n'.join(sorted(words_l)))

    elif action == 3:
        word = str(input('What word should be inspected?\n'))
        print(f"{dic.inserted(word)} = {len(word)} letters \
/ {len(dic.inserted(word).split('-'))} syllables = \
{len(word)/len(dic.inserted(word).split('-'))} letters per syllable")

    elif action == 4:
        nums = int(input('How many words would you like to go through?\n'))
        info = make_report(nums)
        print("\n\nHere is your report:\n-------------------")
        print(f"The average L/S is: {round(info.avg_score, 3)}, the median: {round(info.med_score)}")
        print('\n')
        print('Raw data preview:')
        if len(info.alphabetized_data) > 10:
            print(f"[{' '.join(info.alphabetized_data[:5])}... ...{' '.join(info.alphabetized_data[-5:])}]")
        else:
            print('['+' '.join(info.alphabetized_data)+']')
        print('-----End of report-----')

    elif action == 5:
        lorem_ipsum = []
        sentences = randint(3, 7)
        for _ in range(sentences):
            words = randint(9, 15)
            lorem_ipsum.append(gen_new_word(0))
            for _1 in range(words-2):
                lorem_ipsum.append(gen_new_word(0).lower())
                lorem_ipsum[-1] += ',' if choice(range(3)) == 1 else ''
            lorem_ipsum.append(gen_new_word(0).lower())
            lorem_ipsum[-1] += choice(['.']*8 + ['!']*4 + ['?']*3 + ['‽'])
        print(' '.join(lorem_ipsum))
    wait(2.4)
