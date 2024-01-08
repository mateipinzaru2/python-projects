"""
APPENDING IN PYTHON
It's common to create an empty list then fill it with values using a loop. We can add values to the end of a list using the .append() method:

cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']

ASSIGNMENT
We need to generate a unique user ID for each player in the game. An ID is just a unique number that identifies a user.

Let's finish the generate_user_list function. Use the body of the loop to add the unique ID's to the player_ids list.
"""

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids
