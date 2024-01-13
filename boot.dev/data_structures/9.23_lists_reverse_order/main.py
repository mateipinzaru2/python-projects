"""
REVERSE LIST
ASSIGNMENT
Some of our players would like to view their inventories in reverse order.

Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

For example:

[1, 2, 3] -> [3, 2, 1]
['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

TIP
The Python range function is very useful when working with lists. Alternately, you may want to use list slicing.

Where should you start your loop from?
Where should you end your loop?
What should the step be? In other words, how should you increment i in each iteration of the loop?
"""

# CONS:
# - O(n) time complexity
# - modifies input array
def reverse_array(items):
    reverse = []
    for i in range(0, len(items)):
        reverse.append(items.pop())
    return reverse

# CONS:
# - O(1) time complexity
# PROS:
# - doesn't modify input array
def reverse_array_alt(items):
    reverse = []
    for i in range(len(items) - 1, -1, -1):
        reverse.append(items[i])
    return reverse

# BEST SOLUTION:
def reverse_array_pythonic(items):
    return items[::-1]
