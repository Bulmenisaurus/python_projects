import math


def fibionacci(up_to):
    fibionacci_list = [0, 1]
    while fibionacci_list[len(fibionacci_list)-1] < up_to:
        fibionacci_list.append(fibionacci_list[::-1][0]+fibionacci_list[::-1][1])
    return fibionacci_list


def compact(number):
    number = int(number)
    compact_options = []
    if number in fibionacci(number):
        compact_options.append("F"+str(fibionacci(number).index(number)))
    if str(number)[::-1][0] == "0":
        count = 0
        for y in [z == "0" for z in str(number)][::-1]:  # determines how many 0's in a row are at the end of a number
            if y:
                count += 1
            else:
                break
        compact_options.append(f"L{str(number)[0:len(str(number))-count]},{count}")  # l for logarithm
    if int(max(list(str(number)))) < 9:
        converted = int(str(number), base=int(max(list(str(number)))) + 1)
        compact_options.append(f"B{int(max(list(str(number)))) + 1},{converted}")  # B for base
    if number % 2 == 0:
        compact_options.append(f"E{number//2}")  # E for even)
    else:
        compact_options.append(f"O{(number-1)//2}")  # O for odd
    print(compact_options)


compact(input())
