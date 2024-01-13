"""
DIFFERENCES
Your local gym recently bought out another gym, and they're trying to merge their customer data. You've been given 2 lists of customer IDs (numbers) and are trying to figure out which customers from the first gym are not also members of the second gym. Luckily, the IDs from the 2 gyms match up because they used the same back-end servers.

CHALLENGE
Complete the find_missing_ids function. It accepts two lists as input, and returns a new list of all the ids present in the first list but not the second.

Keep in mind, there may be duplicate ids in these lists, the gym workers aren't exactly concerned about data integrity. Make sure to remove any duplicates.

TIP
You can convert a List to a Set using the set() function.
You can convert a Set to a List using the list() function.
You can subtract the elements in one Set from another Set using the - operator.
"""


def find_missing_ids(first_ids, second_ids):
    if not isinstance(first_ids, list) or not isinstance(second_ids, list):
        raise TypeError("Both arguments must be lists")

    first = set(first_ids)
    second = set(second_ids)
    difs = first - second
    return list(difs)
