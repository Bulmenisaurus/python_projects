def factorial(num):
    factorial_sum = 1
    for x in range(1, num):
        factorial_sum *= x
    return factorial_sum


factorial_num = str(factorial(100))
print(sum(int(d) for d in factorial_num))
