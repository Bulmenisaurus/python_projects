"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

index is list index + 1

fibionacci[0] = 0
fibionacci[1] = 1
fibionacci[2] = 1

"""


def calc_next_fibi(fibi: list) -> list:
    fibi.append(fibi[-1] + fibi[-2])
    return fibi


fibionacci = [0, 1]
while len(str(fibionacci[-1])) != 1000:
    fibionacci = calc_next_fibi(fibionacci)

#print(fibionacci[-1])
print(len(fibionacci))

