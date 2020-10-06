from random import shuffle, randint


def gen_from_adj(adj_list): #abcdefghijklmnopqrstuvwxyz
    spell = ''
    consonants = list('bcdfghjklmnpqrstvwxz')
    vowels = list('aeiouy')
    for count, test in enumerate(adj_list):
        if len(test) < 3:
            del adj_list[count]
    if len(adj_list) >= 5:
        print('\n'.join(adj_list))
    else:
        return 'error: not enough words. Make sure all 5 words are over the length of 3.'
    shuffle(adj_list)
    for count, word in enumerate(adj_list):
        if not count == len(adj_list)-1:
            search = is_vowel(adj_list[count+1][0], reverse=True)
            if randint(0, 2):
                pointer = 1
                for x in range(len(word)):
                    if is_vowel(word[x]) == search:
                        spell += word[:pointer]
                    else:
                        pointer += 1
                        continue
                    break

            else:
                pointer = len(word)-2
                for x in range(len(word)):
                    if is_vowel(word[x]) == search:
                        spell += word[pointer:]
                    else:
                        pointer -= 1
                        continue
                    break
        else:
            spell += word
    return spell

def is_vowel(letter, reverse=False):
    letter = letter.lower()
    consonants = list('bcdfghjklmnpqrstvwxz')
    vowels = list('aeiouy')
    if not reverse:
        return 'vowel' if letter in vowels else 'consonant'
    else:
        return 'consonant' if letter in vowels else 'vowel'




adj_inputs = []
for x in range(5):
    adj_inputs.append(input(f'Enter an adjective that this spell will make you! \
({5-x} ajectives remaining.)\n').strip().lower().replace(' ', ''))
print(adj_inputs)
spell_final = gen_from_adj(adj_inputs) + ' '
print(((spell_final * 10) + '\n')* 100)

