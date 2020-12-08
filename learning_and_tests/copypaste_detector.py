from random import choice, randint


def copypaste_encode(text: str, min_inserted=0, max_inserted=5):
    encoded = ''
    hidden_chars = ['\u200b', '\u200c', '\u200d', '\u2060', '\ufeff', '\u2063', '\u2062']
    for letter in text:
        encoded += letter + ''.join([choice(hidden_chars) for _ in range(randint(max_inserted, max_inserted))])
    return encoded


words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret ' \
        'fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon ' \
        'python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad ' \
        'trout turkey turtle weasel whale wolf wombat zebra'.split()

word = choice(words).upper()
word_uncopy = copypaste_encode(word, min_inserted=1)

print('Please either write the word below or copy-paste it. This program can tell if you used copy paste or not!')
print(word_uncopy)
