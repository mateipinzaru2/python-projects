"""
FIND MAX
INFINITY
The built-in float() function can be used to create a numeric floating point value that represents the negative infinity value. Because every value will be greater than negative infinity we can use it to help us accomplish our goal of finding the max value. I've added it for you as a starting point.

negative_infinity = float('-inf')
positive_infinity = float('inf')

ASSIGNMENT
Our players want a way to see their strongest attack from their last combat. Let's add another function to analyze data from our combat log.

Complete the find_max function that looks at each number in the nums list and returns the maximum value. If no maximum is found it just returns negative infinity.

EXAMPLE
find_max([100, 10, 22])
# returns 100
"""

def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far
