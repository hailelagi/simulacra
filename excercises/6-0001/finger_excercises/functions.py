"""
Write a function isIn that accepts two strings as arguments and returns
True if either string occurs anywhere in the other, and False otherwise
"""


def isIn(str_one, str_two):
    return (str_one in str_two) or (str_two in str_one)