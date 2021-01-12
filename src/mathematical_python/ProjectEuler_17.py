from math import ceil

def len_word(number):
    number_list = list(str(number))
    if len(number_list) in (1, 2):
        slicetens = ''.join(number_list)
    else:
        slicetens = ''.join(number_list[1:3])
    immovable_slice = slicetens
    if 9 < int(slicetens) < 20:
        del number_list[0]
        del number_list[-1]
        case = {
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
        }
        number_list.append(case[int(slicetens)])
    elif int(slicetens[-1]) < 10:
        del number_list[-1]
        case = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
        }
        number_list.append(case[int(slicetens[-1])])
    if len(str(immovable_slice)) == 2 and int(immovable_slice) not in list(range(10, 20)):
        if len(str(number)) == 3:
            del number_list[1]
            insertion = 1
        else:
            del number_list[0]
            insertion = 0
        case = {
            0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty',
            5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
        }
        number_list.insert(insertion, case[int(slicetens[0])])
    if len(str(number)) == 3:
        del number_list[0]
        case = {
            0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
        }
        number_list.insert(0, case[int(str(number)[0])]+'hundred')
    if int(slicetens) == 0 or (len(slicetens) == 2 and slicetens[1] == '0'):
        if len(str(number)) == 3:
            if int(slicetens) == 0:
                number_list[1:3] = ['', '']
            else:
                number_list[3] == ''
        elif len(str(number)) == 2:
            number_list[1] = ''
    return ''.join(number_list)


while True:
    print(len_word(input('What would you like to letterfy?\n')))