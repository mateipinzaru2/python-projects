"""
MINIMUM NUMBER IN PYTHON
ASSIGNMENT
Write a function called find_min() that finds the smallest number in a list

find_min([1, 3, -1, 2]) -> -1

find_min([18, 3, 7, 2]) -> 2

POSITIVE INFINITY
Since you're trying to keep track of the smallest number, start with a really big number. Python has a built-in constant that represents positive infinity.

min = float("inf")
"""


def find_min(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not nums:
        raise ValueError("List is empty")
    for n in nums:
        if not isinstance(n, (int, float)):
            raise ValueError("Only numbers allowed")
    min_num = float("inf")
    for n in nums:
        if n < min_num:
            min_num = n
    return min_num
