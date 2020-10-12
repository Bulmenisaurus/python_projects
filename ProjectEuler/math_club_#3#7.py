"""Original problem
`The secret code is an integer number which ends with “2” (that means its rightmost digit is 2.)
 If you cross  out this 2 and write it in front of the code instead,
 you get a number that is twice as big as the original  one. What was the original secret code?
`
"""

for x in range(1000000  ):
    x = x*19
    str_x = list(str(x))
    if str_x[-1] == '0':
        continue
    str_x.insert(0, str_x[-1])
    if str_x[:-2] == list(str(x*2)):
        print(x)
