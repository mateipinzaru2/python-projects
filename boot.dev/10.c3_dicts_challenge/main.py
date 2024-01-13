"""
GROCERY SHOPPING
Emma has been overspending recently and wants you to write a script that will help her manage her finances when she's grocery shopping.

CHALLENGE
Complete the calculate_total function.

INPUTS
items_purchased: A list of the names of items purchased on this shopping trip. This is a list of strings.
grocery_list: A list of the names of items Emma wanted to purchase. This is also a list of strings.
OUTPUTS
The function should return 3 values in this order:

unpurchased_items: A list of all the item names in grocery_list that weren't found in items_purchased.
receipt: A dictionary containing all the items Emma purchased, even stuff not on her list. The keys are the item names and the values are their respective prices from the item_prices dictionary.
total: The total cost of all the items that were purchased.
Return each value separately, not in a list. For example:

return item1, item2, item3

Note: The .remove() list method may be helpful.
"""


def calculate_total(items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }

    # Don't touch above this line

    unpurchased_items = []
    for item in grocery_list:
        if item not in items_purchased:
            unpurchased_items.append(item)

    total = 0
    receipt = {}
    for item in items_purchased:
        if item in item_prices:
            receipt[item] = item_prices[item]
            total += item_prices[item]

    return unpurchased_items, receipt, total
