"""
Recursion refers to the repeated applications of the same function.

Problems are solved by solving smaller instances of the same problem.
"""

# Solving the Fibonacci problem
# Fibonacci sequence = [0,1,1,2,3,5,8...]
# Given a position find the fibonacci value in the array


def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

# Solving Factorials
# Factorial sequence = 5! = 120


def factorial(value):
    if value == 0:
        return 1
    return value * factorial(value - 1)
