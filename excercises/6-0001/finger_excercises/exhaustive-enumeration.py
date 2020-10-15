"""
Write a program that asks the user to enter an integer and prints
two integers, root and pwr, such that 0 < pwr < 6 and root ** pwr
is equal to the integer entered by the user. If no such pair of
integers exists it should print a message to that effect
"""

userInt = int(input("Enter an integer"))

# imperative solution
maxPwr = 6
while maxPwr >= 0:
    root = userInt ** 0.5
    if (root ** maxPwr) == userInt:
        print(f"root={root}", f"pwr={userInt ** maxPwr}")

print("no such pair exists")
