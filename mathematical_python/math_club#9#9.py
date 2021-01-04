num = "1234567890" * 10

newnum = ''
print(num)

for x in range(10):
    for i in range(len(num)):
        if (i+1) % 2 == 0:
            newnum += num[i]
    print(''.join([j if j in newnum else '_' for j in "1234567890"*10]))
    num = newnum
    newnum = ''
