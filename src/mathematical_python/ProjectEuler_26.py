def principal_period(s):  # from https://stackoverflow.com/a/29489919/
    i = (s+s).find(s, 1, -1)
    return '' if i == -1 else s[:i]


result = (0, 0)  # first, x, then the number of repeating decimals
for x in range(1, 1000):
    possible_num = str(1/x)[2:]
    repeating_decimal_pattern = max(len(principal_period(possible_num[i:])) for i in range(200))

    if x % 5 == 0:
        print(f"1/{x} = {possible_num} = {repeating_decimal_pattern} digits")

    if repeating_decimal_pattern > result[1]:
        result = (x, repeating_decimal_pattern)

print(result)