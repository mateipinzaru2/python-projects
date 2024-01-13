"""
ASSIGNMENT
Fix the bug in the sum_of_numbers function. Instead of adding 1 to total at each iteration of the loop, it should add i. For example, instead of:

1 + 1 + 1 + 1 + 1...

we want:

0 + 1 + 2 + 3 + 4...

The desired output is a single number after the loop has finished executing.
"""

def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total
