"""
ASSIGNMENT
Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
Next, return a slice of the champions list that starts at the beginning of the list and ends with the third champion from the end (inclusive).
Last, return a slice of the champions list that only includes the champions in even numbered indexes.
TIP
Remember, you can return multiple values from a function by separating them with commas:

return value1, value2, value3
"""

def get_champion_slices(champions):
    first_list = champions[2:]
    second_list = champions[:-2]
    third_list = champions[::2]
    return (
        first_list,
        second_list,
        third_list
    )
