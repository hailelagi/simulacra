"""
Write a program that asks the user to input 10 integers and then
prints the largest odd number that was entered. If no odd number was
entered, it should print a message to that effect
"""

# declarative solution
"""
nums = [input("enter a number") for num in range(10)]
odd_nums = filter(lambda num: int(num) % 2 == 1, nums)
print(max(odd_nums, default="all nums even"))
"""

# imperative solution using while iteration
count = 10
userInts = []

while count > 0:
    userInteger = int(input("enter a number"))
    if userInteger % 2 == 1:
        userInts.append(userInteger)

    count -= 1

print(max(userInts, default="all nums even"))
