"""
LIST LENGTH
The length of a List can be calculated using the len() function.

fruits = ["apple", "banana", "pear"]
length = len(fruits)
# Prints: 3

The length of the list is equal to the number of items present. Don't be fooled by the fact that the length is not equal to the index of the last element, in fact, it will always be one greater.

ASSIGNMENT
Some of our player's inventories are huge, so looking through the entire list is cumbersome. Let's find an easy way for us to get the index of the last item in their inventory.

Complete the get_last_index function so that it returns the length of the inventory list minus 1.
"""

def get_last_index(lst):
    return len(lst) - 1
