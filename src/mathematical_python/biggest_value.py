"""
Drag a digit into each box. Evaluate your expression. Try to find the result closest to 0.

[] * []^[] - []([] + [])
"""
from itertools import permutations

TEMPLATE = "({} + {} * {}) / ({} - {})"
PERMUTATIONS = list(permutations([3, 5, 4, -3, -4, -5, -2, 2]))

largest = []
for perm in PERMUTATIONS:
    try:
        largest.append((eval(TEMPLATE.format(*perm)), TEMPLATE.format(*perm[:5])))
    except ZeroDivisionError:
        pass


print("Closest equation to 0:\n")
solution = sorted(largest, key=lambda x: x[0])[::-1][1]
print(f"{solution[1]} = {solution[0]}", '\n\n')


