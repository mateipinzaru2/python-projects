"""
WHAT IS OBJECT-ORIENTED PROGRAMMING?
Object Oriented programming, or "OOP" for short, is a way of writing code that relies on the concepts of classes and objects. The main benefit of writing your code in an object-oriented way is to structure your program into simple, reusable pieces of code.

In this course, we'll be coding the pieces of a real-time strategy game called "Age of Dragons". Players will control armies of people, elves, orcs, and dragons as they fight with one another online. If you're familiar with Age of Empires, WarCraft, or StarCraft, it will be something like that.

ASSIGNMENT
Your manager has noticed that there's a lot of repetitive code in the "Age of Dragons" code base. She has tasked you with reworking the fight_soldiers function so that the DPS (damage-per-second) calculation logic is only written once.

Notice how these two lines are practically identical:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]

We removed these lines from the fight_soldiers function and replaced them with calls to get_soldier_dps. Finish the get_soldier_dps function so it uses the same logic as the lines above. get_soldier_dps should take a soldier, which is a dictionary, and return its DPS.
"""


def get_soldier_dps(soldier):
    if (
        isinstance(soldier, dict)
        and "damage" in soldier
        and "attacks_per_second" in soldier
    ):
        output = soldier["attacks_per_second"] * soldier["damage"]
        return output
    else:
        return 0


def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"
