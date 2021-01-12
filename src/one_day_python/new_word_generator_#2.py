"""
Open file, extract data
Add letters of each word, append to dictionary
build new words off of that
"""
import string
from random import shuffle, choice


def extract_wordpatterns(wordpattern_data):
    valid_letters = string.ascii_letters

    wordpatterns = {i: "" for i in "| "+string.ascii_lowercase}  # initialize empty alphabet {a="", b="", etc}
    for wrd in wordpattern_data:
        wrd = wrd.lower()
        for index, lttr in enumerate(wrd):
            try:  # detect if lttr is last
                wrd[index+1]
            except IndexError:
                # This code is run when lttr is the last letter in a word
                wordpatterns[lttr] = '|'  # (should) mean End of word
            else:
                if lttr in valid_letters:
                    # This code is run when lttr isn't
                    wordpatterns[lttr] += wrd[index+1]
                if index == 0:
                    wordpatterns['|'] += lttr  # beginning of word

    wordpatterns = {i: ''.join(sorted(wordpatterns[i])) for i in wordpatterns}
    return wordpatterns


def gen_words_from_patterns(word_patterns, amount=1, min_len=2, capitalize=False):
    words = []
    while not len(words) >= amount:
        word = choice(word_patterns['|'])
        while True:
            print(f"{word_patterns[word[-1]]=}, {word}")
            new_letter = choice(word_patterns[word[-1]])
            word += new_letter
            if word[-1] == '|':
                break
        if len(word) > min_len:
            words.append(word.capitalize() if capitalize else word)
    return words


with open("../python_data/Dictionary.txt", "r") as dict_:
    data_ = dict_.read().splitlines()

word_data = extract_wordpatterns(data_)
print(word_data)
generated_words = gen_words_from_patterns(word_data, amount=300, min_len=3, capitalize=True)
print(a := [x.replace('|', '').lower() for x in sorted(generated_words)])






