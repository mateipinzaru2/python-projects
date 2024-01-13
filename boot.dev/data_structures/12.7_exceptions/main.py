"""
DIFFERENT TYPES OF EXCEPTIONS
We haven't covered classes and objects yet, which is what an Exception really is at its core. We'll go more into that in the object-oriented programming course that we have lined up for you next.

For now, what is important to understand is that there are different types of exceptions and that we can differentiate between them in our code.

SYNTAX
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)

Which will print:

0 division
index error

As you can see in the example above, we can print the exception message by aliasing the exception using the as keyword.

ASSIGNMENT
Take a look at the get_player_record function. It raises an exception for negative player_id's.

Complete the handle_get_player_record() function. It should return the result of get_player_record but if an IndexError is raised it will instead return the string: index is too high. Otherwise, if any other exception is raised it will just return the exception itself.
"""


def handle_get_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e


# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
