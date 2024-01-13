"""
INDEXING INTO LISTS
Now that we know how to create new lists, we need to know how to access specific items in the list.

We access items in a list directly by using their index. Indexes start at 0 (the first item) and increment by one with each successive item. The syntax is as follows:

best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
print(best_languages[1])
# prints "Go", because index 1 was provided

ASSIGNMENT
We need to allow our players to access items in their inventories!

Fix our get_leather_straps function by changing the value of item_index to the index in inventory that holds the value "Leather Scraps".
"""

def get_leather_straps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]
