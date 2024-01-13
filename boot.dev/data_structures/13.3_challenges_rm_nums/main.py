"""
REMOVE NUMBERS
Complete the remove_nonints() function that takes a list and returns a new list with all the non-integer types removed.

remove_nonints(['1', 1, '3', '400', 4, 500])
# Remaining list after removing nonints = [1, 4, 500]

You can check the type of a variable using type() function

if type(variable) == int:

Do not change the input nums list, return a new list with only the integers.
"""


def remove_nonints(nums):
    output = []
    for elem in nums:
        if isinstance(elem, int) and not isinstance(elem, bool):
            output.append(elem)
    return output


# In Python, bool is a subclass of int, so isinstance(True, int) and isinstance(False, int) both return True.


# alternate solution
# def remove_nonints(nums):
#     output = []
#     for elem in nums:
#         if type(elem) == int:
#             output.append(elem)
#     return output
