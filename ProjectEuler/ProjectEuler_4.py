palindromes = []
for x in range(100, 999):
    for i in range(100, 999):
        if str(x*i) == str(x*i)[::-1]:
            palindromes.append(x*i)
print(sorted(palindromes)[::-1])