import random
from functools import reduce  # reduces the darn fudgin lists (for loops are FOR losers)


def radix_sort(radix_input):
    radixGIF = []
    radix_sorted = buckets(0, radix_input)
    radixGIF.append(radix_sorted)
    for x in range(len(str(max(radix_input)))-1):  # repeats the sort for each digit in the biggest number
        radix_sorted = buckets(x+1, radix_sorted)
        radixGIF.append(radix_sorted)
    return radix_sorted


def buckets(digit, bucket_radix):
    buckets_list = []
    for x in range(10):
        buckets_list.append([])  # sets up the buckets
    for x in bucket_radix:
        x = str(x)
        if len(x) <= digit:
            buckets_list[0].append(int(x))  # if digits[x] is outside of x, input 0 by default
        else:
            buckets_list[int(x[::-1][digit])].append(int(x))
    return reduce(lambda x, y: x+y, buckets_list)  # flattens out any nested lists


length = int(input("How many integers long would you like your list to be?\n"))  # length of list
random_list = [random.randint(0, length) for i in range(length)]  # shuffled list
GIFradix = radix_sort(random_list)
print(GIFradix == sorted(random_list))