def collatz(x):
    chain = 0
    while x != 1:
        chain += 1
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
    return chain

max = 0
for b in range(1, 1_000_001):
    if collatz(b) > max:
        max = collatz(b)
        max_func = b
    if b % 1000 == 0:
        print(b)
print(max_func)
print(max)