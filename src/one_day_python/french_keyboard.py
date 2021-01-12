def french_encode(text):
    old = "abcdefghijklmnopqrstuvwxyz"
    new = "qbcdefghijkl,noparstuvzxsyw"
    result = [new[old.index(x)] if x in old else x for x in text]
    return ''.join(result)


def french_decode(text):
    new = "abcdefghijklmnopqrstuvwxyz"
    old = "qbcdefghijkl,noparstuvzxsyw"
    result = [new[old.index(x)] if x in old else x for x in text]
    return ''.join(result)


print(french_encode(input("french encode boiii\n")))
print(french_decode(input("french decode boiii\n")))

