"""
Replace the comment in the following code with a while loop.
numXs = int(input('How many times should I print the letter X? '))
toPrint = "
#concatenate X to toPrint numXs times
print(toPrint)
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ""

while numXs > 0:
    toPrint += "X"
    numXs -= 1

print(toPrint)
