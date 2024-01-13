"""
FIRST ELEMENT
ASSIGNMENT
Let's add another function to our inventory system. Write a function that returns the first element from a list. If the list is empty then return the string ERROR instead.
"""

def get_first_item(items):
    if not len(items):
        return "ERROR"
    return items[0]
