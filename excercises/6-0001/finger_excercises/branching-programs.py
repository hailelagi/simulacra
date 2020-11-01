"""
Write a program that examines three variables - x,y & z -- and
prints the largest odd number among them. If none of them are
odd, it should print a message to that effect.
"""
import random

x = random.randint(1, 100)
y = random.randint(1, 100)
z = random.randint(1, 100)

# declarative solution
# print(max(filter(lambda a: a % 2 == 1 or a == 1, [x, y, z]), default="all nums even"))

# imperative solution
# using branching logic only
if x > y and x > z and x % 2 == 1:
    print(x)
elif y > z and y % 2 == 1:
    print(y)
elif z % 2 == 1:
    print(z)
else:
    if x or y or z == 1:
        print(1)
    else:
        print("all numbers are even", x, y, z)
