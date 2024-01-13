"""
LIST DIVISION
Write a function called divide_list() that takes a list and a number as input. The function returns a new list that contains all the elements of the original list except they have been divided by the second input.

divide_list([6, 8, 10], 2)
# [3.0, 4.0, 5.0]

Make sure you're appending the raw float values. Don't round or cast the numbers to integers.
"""


def divide_list(nums, divisor):
    if (
        not isinstance(nums, list)
        or not isinstance(divisor, int)
        or not all(isinstance(n, int) for n in nums)
    ):
        raise TypeError("Input must be a list of integers and a single integer")
    output = []
    for n in nums:
        if divisor != 0:
            result = n / divisor
            output.append(result)
        else:
            raise Exception("can't divide by 0")
    return output
