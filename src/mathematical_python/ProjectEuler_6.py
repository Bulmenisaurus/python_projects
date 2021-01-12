sum_of_squares = sum([x*x for x in range(1, 101)])
square_of_sum = sum(x for x in range(1, 101)) * sum(x for x in range(1, 101))

print(square_of_sum-sum_of_squares)
