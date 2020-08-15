import random


def radix_sort(radix_input):
    radix_sorted = buckets(0, radix_input)


def buckets(digit, bucket_radix):
    buckets_list = []
    for x in range(10):
        buckets_list.append([])  # sets up the buckets
    for x in bucket_radix:
        x = str(x)
        if len(x) < digit:
            buckets_list[0].append(0)  # digits[x] is outside of x, input 0 by default
        else:
           buckets_list[int(x[::-1][digit])].append(int(x))
    print(buckets_list)
    return buckets_list


length = int(input("How many integers long would you like your list to be?\n"))  # length of list
random_list = [random.randint(0, length) for x in range(length)]  # shuffled list
print(random_list)
radix_sort(random_list)
