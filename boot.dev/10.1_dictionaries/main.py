"""
DICTIONARIES
Dictionaries in Python are used to store data values in key -> value pairs. Dictionaries are a great way to store groups of information.

car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}

ASSIGNMENT
Complete the get_character_record function. It takes a character's name, server, level, and rank as individual inputs, and returns a dictionary with the following keys:

name
server
level
rank
id
Each key should map to its corresponding input, except the id key. The id key map to the name and the server inputs concatenated with a # in the middle for uniqueness. We can't have two bloodwarrior123's on the same server!

For example, given:

name = bloodwarrior123
server = server1
Then the id field should be set to bloodwarrior123#server1. I recommend using an f-string to create the id field.
"""


def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }
