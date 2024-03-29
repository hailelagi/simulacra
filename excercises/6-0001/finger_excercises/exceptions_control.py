"""
Implement a function that satisfies the specification
"""


def findAnEven(L):
    """
    :Assumes L is a list of integers:
    :Returns the first even number in L:
    :Raises ValueError if L does not contain an even number:
    """
    for num in L:
        if num % 2 == 0:
            return num

    raise ValueError
