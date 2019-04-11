#sandygcabanes
#w3resources.com
#mini project plotting histogram of random numbers
''' It seems that the random answers are not equally distributed.
So I decided to investigate'''

import random
import matplotlib

def computeTicks (x, step = 1):
    """  from stackoverflow by Greenstick Jul 28 '17 at 20:55
    Computes domain with given step encompassing series x
    x    - Required - A list-like object of integers or floats
    step - Optional - Tick frequency
    """
    import math as Math
    xMax, xMin = Math.ceil(max(x)), Math.floor(min(x))
    dMax, dMin = xMax + abs((xMax % step) - step) + (step if (xMax % step != 0) else 0), xMin - abs((xMin % step))
    return range(dMin, dMax, step)

list_of_random_numbers = []
i = 0
while i < 100:
    a = random.randint(1,20)
    list_of_random_numbers.append(a)
    i += 1
print ('list of random numbers', list_of_random_numbers)

import matplotlib.pyplot as plt
plt.hist(list_of_random_numbers, bins = 20)
plt.xticks(computeTicks(list_of_random_numbers))
plt.show()
