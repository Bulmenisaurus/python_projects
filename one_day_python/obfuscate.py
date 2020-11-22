"""
The aim if this project is to be able to make code
hard to read, undecipherable
"""

from random import shuffle, randint, getrandbits, choice
import string


def obfuscate_num(num: int):
    """Obfuscate numbers effectively"""

    def uni_obfuscate(num_: int):
        """Obfuscating using ord() and chr()"""
        try:
            return "ord("+repr(str(chr(num_)))+")"
        except ValueError:
            return

    def set_obfuscate(num_: int):
        """Using x unique characters and sets"""
        if num_ < 0:
            return

        unique_characters = list(string.printable)if getrandbits(1) or num > 10 else list('{[)_,.><\"\'')
        shuffle(unique_characters)
        unique_characters = list(''.join([k * randint(1, 7) for k in unique_characters[:num_]]))
        shuffle(unique_characters)
        if getrandbits(1):
            return "len(set("+repr(''.join(unique_characters))+"))"
        else:
            return repr(unique_characters).replace('[', '{').replace(']', '}')+"__len__()"

    def bit_obfuscate(num_: int):
        """Uses << and >> operators to make seemingly improper equations (to non programmers)"""
        offset = randint(0, 50)
        return str(num_ << offset) + " >> " + str(choice([set_obfuscate(offset), uni_obfuscate(offset), offset]))

    def boolsum_obfuscate(num_: int):
        """Worst ducking thing here, sum of a number of booleans"""

        if num_ < 0:
            return
        trues, falses = (num_ if num_> 0 else 0, -num_ if num_ < 0 else 0)
        truffset = randint(*sorted((num_//2, -num_//3)))  # adds random number of trues or falses
        trues += truffset
        falses += -truffset
        bool_list = [True]*trues+[False]*falses
        shuffle(bool_list)

        return "sum("+repr(bool_list)+")"

    choices = []
    funcs = [uni_obfuscate, set_obfuscate,
             bit_obfuscate, boolsum_obfuscate,
             ]
    for x in funcs:
        if (obfuscated_choice := x(num)) is not None:
            choices.append(obfuscated_choice)

    return choice(choices)


print(obfuscate_num(32000))
