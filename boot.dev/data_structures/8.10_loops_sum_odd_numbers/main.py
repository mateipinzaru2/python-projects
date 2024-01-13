"""
SUM GAME 2
ASSIGNMENT
Complete the sum_of_odd_numbers function. It should calculate the sum of all the odd numbers starting at 1 up to (but not including) the given end number and return the result.

TIPS
What number should you start with if you only want odd numbers?
How much should you increment by in each iteration of the loop to get the next odd number?
"""

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total
