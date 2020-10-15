"""
What would the code in fig 3.4 do if the statement x = 25 were replaced
by x = -25?
"""

"""
What would have to be changed to make the code in Figure 3.4 work for 
finding an approximation to the cube root of both negative and positive
numbers? (Hint: think about changing low to ensure that the answer lies
within the region being searched)
"""

# bisection search
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans ** 2 - x) >= epsilon:
    print(f"low ={low}", f"high ={high}", f"ans ={ans}")
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print(f"numGuesses ={numGuesses}")
print(f"{ans} is close to square root of {x}")
