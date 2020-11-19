import random
import matplotlib.pylab as pylab

vals = []
for _ in range(1000):
    num1 = random.choice(range(0, 101))
    num2 = random.choice(range(0, 101))
    vals.append(num1 + num2)

pylab.hist(vals, bins=10)
pylab.ylabel("Number of occurrences")
pylab.show()

"""
Why are bins near the middle of the 
histogram taller than the bins near the
sides? Hint: think about why 7 is the 
most common outcome of rolling a pair
of dice.
"""

"""

"""