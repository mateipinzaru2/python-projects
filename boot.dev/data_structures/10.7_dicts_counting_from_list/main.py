"""
COUNTING PRACTICE
CHECKING FOR EXISTENCE
If you're unsure whether or not a key exists in a dictionary, use the in keyword.

cars = {
    'ford': 'f150',
    'tesla': '3'
}

print('ford' in cars)
# Prints: True

print('gmc' in cars)
# Prints: False

ASSIGNMENT
We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. Complete the count_enemies function. It takes a list of enemy names as input. It should return a dictionary where the keys are all the enemy names from the list, and the values are the counts of how many times each enemy appeared in the list.
"""


def count_enemies(enemy_names):
    output = {}
    for enemy in enemy_names:
        if enemy in output:
            output[enemy] += 1
        else:
            output[enemy] = 1
    return output
