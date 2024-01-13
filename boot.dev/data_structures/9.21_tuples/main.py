"""
ASSIGNMENT
The "Fantasy Quest" character system needs a list of "heroes" to be able to run the game properly. Someone wrote some pretty nasty code, and the code in question creates a heroes list where every 3rd index defines a new hero. First their name, then their age, then whether or not they're an "elf".

Change the heroes list declaration from its current state to a list of tuples. Use the same data for each hero, and order it in the same way.
"""

def get_heroes():
    heroes = [
        (
            "Glorfindel",
            2093,
            True
        ),
              
        (
            "Gandalf",
            1054,
            False
        ),
        
        (
            "Gimli",
            389,
            False
        ),
        
        (
            "Aragorn",
            87,
            False
        )
    ]

    return heroes


# Don't touch below this line


def test():
    heroes = get_heroes()
    for hero in heroes:
        print(f"name: {hero[0]}, age: {hero[1]}, is_elf: {hero[2]}")


def main():
    test()


main()
