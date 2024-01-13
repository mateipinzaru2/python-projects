"""
ITERATING OVER A DICTIONARY IN PYTHON
fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny

ASSIGNMENT
We need to display on our player's screens what the most common enemy in a given area of the game map is.

Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count. If there are no enemies, return None.

enemies_dict is a dictionary of name -> count.

TIP: NEGATIVE INFINITY
When you're trying to find a "max" value, it helps to keep track of the "max so far" in a variable and to start that variable at the lowest possible number, negative infinity.

max_so_far = float("-inf")

You'll also want to keep track of the enemy name associated with the maximum count. I would set the default for that variable to None.
"""


def get_most_common_enemy(enemies_dict):
    name = None
    max_so_far = float("-inf")
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]
            name = enemy
    return name
