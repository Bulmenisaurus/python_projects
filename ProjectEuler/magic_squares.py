from itertools import permutations
from math import sqrt, floor

create_list_len = int(input("How many squares does this magix square contain (3, 9, 81, etc)?\n"))
create_list_min = int(input("What is the smallest number in your list? \
(this program assumes all values appear once)?\n"))
create_list = [x+create_list_min for x in range(create_list_len)]

if floor(sqrt(len(create_list))) != sqrt(len(create_list)):
    print("Length of list is not a square, and therefore, cannot be a magic one")

print("Calcing perms")
create_list_perms = list(permutations(create_list))
#print(create_list_perms)


print("Gen_matrix init")
def gen_matrix(num_list):
    side_len = int(sqrt(len(num_list)))
    matrix = [[''] * side_len for x in range(side_len)]
    for row in range(side_len):
        for row_n in range(side_len):
            matrix[row][row_n] = num_list[row * side_len + row_n]
    print(matrix)

print("Gen_matrix call")
gen_matrix(create_list)
