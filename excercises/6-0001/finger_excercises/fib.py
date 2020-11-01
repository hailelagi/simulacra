"""
When the implementation of fib in Figure 4.7 is used to compute fib(5),
how many times does it compute the value o fib(2) on the way to computing
fib(5)?
"""


"""
Computes it 4 times
fib(5) = fib(4) = fib(3) = fib(2) = fib(n - 1) + fib(n - 2)
fib(n) = fib(n - 1) + fib(n -2)
n - 2 is naively recomputed for each fib other than the base case
"""