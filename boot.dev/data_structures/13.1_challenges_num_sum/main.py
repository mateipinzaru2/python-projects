"""
CHALLENGES
In this chapter we are going to practice applying the skills and concepts we learned while building "Fantasy Quest"

NUMBER SUM
Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:

number_sum(5) -> 1+2+3+4+5 -> 15

number_sum(3) -> 1+2+3 -> 6
"""


def number_sum(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum
