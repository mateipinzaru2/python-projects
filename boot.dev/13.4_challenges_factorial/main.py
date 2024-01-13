"""
FACTORIAL
Complete the factorial() function. It should calculate the factorial of a number. A factorial of a number is the product of all positive integers less than or equal to that number.

For example:

4! = 4 * 3 * 2 * 1 = 24

The ! symbol denotes a factorial

TIP: A SPECIAL CASE FOR ZERO
The value of 0! is 1. This keeps factorials consistent with the convention for an empty product.
"""


# with recursion:
def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)


# print(factorial(5000)) # RecursionError: maximum recursion depth exceeded


# Recursive version:
# The recursive version has the overhead of function calls.
# Each recursive call adds a layer to the system call stack.
# This overhead can become significant if the input number is large,
# potentially leading to a stack overflow error if the maximum stack depth is exceeded.


# without recursion:
# def iterative_factorial(num):
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     return factorial
# print(iterative_factorial(5000))  # eventually prints the output but is VERY SLOW


# Iterative version:
# The iterative version uses a simple loop and does not have the overhead of function calls.
# It is generally more efficient in terms of memory usage and can handle larger input numbers
# without risk of a stack overflow.


from sympy import factorial


def sympy_factorial(num):
    return factorial(num)


print(str(sympy_factorial(500)))  # is VERY FAST
