from random import choice


def multiline_input(__prompt):
    print(__prompt)
    input_lines = ['\x00']
    while (line := input()) != '' and input_lines[-1] != '':
        input_lines.append(line)
    return '\n'.join(input_lines)[1:]


def funnify_word(word: str, ending: str) -> str:
    """
    Inserts ending to all words. This account for all
     non-alpha characters and the end of a word.

    :param word: The word to be included. A "word" is just space-seperated strings in sentences
    :param ending: The ending to append to words
    :return: basically word + ending, and accounting for periods, question marks?, etc.

    """
    if word[-1].isalpha():
        return word + ending  # if word ends with a letter, just append the ending
    else:
        for x in range(len(word)-1, -1, -1):   # scans through the word backwards (no while loops lol)
            if word[x].isalpha():              # if we hit upon a letter
                word_list = list(word)         # use list() for .insert() functionality
                word_list.insert(x+1, ending)  # insert the ending at the letter found
                return ''.join(word_list)      # return the finished


sentences = multiline_input("Enter your sentences to funnify!")

vowels = "eyuioa"
consonants = "qwrtpsdfghklzxcvbnm"
funny_ending = input("What is the funny ending? [dont write anything for random]\n") or \
               (choice(consonants) + choice(vowels))

new_sentences = ' '.join([funnify_word(x, funny_ending).strip() for x in sentences.split(' ')])
print(new_sentences)



