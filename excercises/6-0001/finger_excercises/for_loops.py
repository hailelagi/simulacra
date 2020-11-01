"""
Let s be a string that contains a sequence of decimal numbers separated
by commas, e.g., s = "1.23,2.4,3.123". Write a program that prints the sum
of the numbers in s
"""
from functools import reduce

s = "1.23,2.4,3.123"

# imperative solution
total = 0
for n in s.split(","):
    total = total + float(n)

# declarative solution
reduce(lambda acc, num: acc + float(num), s.split(","), 0)
