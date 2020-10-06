print('')
for x in range(123456789, 999999999):
    x_list = [int(j) for j in list(str(x))]
    if not set(range(1, 10)) == set(x_list):
        continue
    for i in range(1, 9):
        ind_1 = x_list.index(i)
        ind_2 = x_list.index(i+1)
        if (ind_1-ind_2)%2==0 and abs(ind_1-ind_2)>1:
            print(x)
