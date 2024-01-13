"""
SETS
Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.

fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

ADD VALUES
fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

Note: No error will be raised if you add an item already in the set.

EMPTY SET
Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.

fruits = set()

ITERATE OVER VALUES IN A SET (ORDER IS NOT GUARANTEED)
fruits = {'apple', 'banana', 'grape'}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple

ASSIGNMENT
Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this by creating a set, adding all the spells to it, then iterating over the set and adding all the spells back into a List and returning the list.

It makes no sense to learn a spell twice! Once it's learned, it's learned forever.
"""


def remove_duplicates(spells):
    return list(set(spells))


# def remove_duplicates(spells):
#     spells_set = set()
#     for spell in spells:
#         spells_set.add(spell)
#     deduped_spells = []
#     for deduped_spell in spells_set:
#         deduped_spells.append(deduped_spell)
#     return deduped_spells
