def decode(to_decode):
    to_decode = str(to_decode)
    key = 'abcdefghijklmnopqrstuvwxyz'
    newstr = ''
    for j in range(len(to_decode)):
        if to_decode[j] in key:
            decode_num = key.index(to_decode[j])-j
            if decode_num < 0:
                decode_num = len(key) - abs(decode_num%26)
                newstr += key[decode_num]
            else:
                newstr += to_decode[j]
    return newstr


def encode(to_encode):
    to_encode = str(to_encode)
    key = 'abcdefghijklmnopqrstuvwxyz'
    newstr = ''
    for j in range(len(str(to_encode))):
        newstr += key[((key.index(to_encode[j]))+j) % len(key)] if (to_encode[j] in key) else to_encode[j]
    return newstr


while True:
    print(encode(input('enc')))
    print(decode(input('dec')))
