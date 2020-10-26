k = 144.0

# Newton raphson --> roots

# x^2 - 24 ≈ 0

epsilon = 0.01
guess = k/2.0
numGuesses = 0

while abs(guess * guess - k) >= epsilon:
    numGuesses += 1
    print(f"I'm guessing {numGuesses} with a guess of {guess}")
    # x(n+1) = f(x(n)) / f'(x(n))
    # where x is a guess, n is numGuesses
    # f(x) = x ^ 2 - 24
    # f'(x) = 2x
    guess = guess - (((guess ** 2) - k)/(2 * guess))

print(f"Square root of {k} is approximatel {guess}")
