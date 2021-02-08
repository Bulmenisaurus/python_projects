"""
What is the largest N such that 12! is divisible by 2^N?
"""

FACTORIAL_12 = 479001600

for x in range(30):
    num = 2 ** x
    if FACTORIAL_12 % num == 0:
        print(num, '2^%s' % x)
