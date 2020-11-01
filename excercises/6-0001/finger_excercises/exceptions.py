"""
Implement a function that meets the specification below.
Use a try-except block.
"""


def sumDigits(s):
    """
    :Assumes s is a string:
    :Returns the sum of the decimal digits in s:
    :For example, if s is 'a2b3c' it returns 5:
    """
    digits = []
    for char in s:
        try:
            digits.append(int(char))
        except ValueError:
            pass
    return sum(digits)


print(sumDigits("a2b3c"))
