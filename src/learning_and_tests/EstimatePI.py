import random
from math import sqrt
import time

dot_iterations = int(input("How many iterations would you like the formula to last?\n"))
dots_in_circle = 0
start = time.time()
for x in range(dot_iterations):
    dot_x, dot_y = random.random()*2 - 1, random.random()*2 - 1  # from -1.00 to 1.00
    dist = (dot_x**2 + dot_y**2)
    if sqrt(dist) <= 1:
        dots_in_circle += 1
print(f"""{dot_iterations} iterations have been completed in {time.time()-start} secs. Our estimation of pi is:
{4 * (dots_in_circle/dot_iterations)}""")
