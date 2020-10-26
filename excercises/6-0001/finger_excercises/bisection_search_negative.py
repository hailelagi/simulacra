"""
What would the code in fig 3.4 do if the statement x = 25 were replaced
by x = -25?

Ans - infinite loop

The roots of a negative number do not converge on a natural number line,
It will keep searching for a root in smaller and smaller intervals forever

because this condition abs(ans ** 2 - x) >= epsilon will always be satisfied
"""

"""
What would have to be changed to make the code in Figure 3.4 work for 
finding an approximation to the cube root of both negative and positive
numbers? (Hint: think about changing low to ensure that the answer lies
within the region being searched)
"""

x = -27
# bisection search - approximate cubic root
imaginary = False

# lol hacked the question with maths
# pretty sure this wasn't the intended answer
if x < 0:
    x = abs(x)
    imaginary = True

epsilon = 0.01
numGuesses = 0
low = 0.0
# ensure root must be > 1
high = max(1.0, x)
ans = (high + low)/2.0

# is this the root you're looking for?
# where epsilon is a random accuracy
while abs(ans ** 3 - x) >= epsilon:
    print(f"low = {low}", f"high = {high}", f"ans = {ans}")
    numGuesses += 1

    if ans ** 3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print("-------RESULT---------")
print(f"numGuesses ={numGuesses}")

if imaginary:
    print(f"{ans * 1j} is close to square root of {x}")
else:
    print(f"{ans} is close to square root of {x}")