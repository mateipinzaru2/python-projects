"""
ROCKET LAUNCH
A team of scientists is getting ready to launch the rockets they have been working on. You've been asked to write a program that will countdown to the rockets' launch.

CHALLENGE
In the countdown_to_blastoff function, write a loop that counts down from 10 to 1. At each iteration, it should print:

NUM...

Where NUM is replaced with the current number in the countdown. However, when NUM is 1, it should instead print:

NUM... Blastoff!
"""

def countdown_to_blastoff():
    for i in range(10, 0, -1):
        if i == 1:
            print(f"{i}... Blastoff!")
        else:
            print(f"{i}...")


# Don't edit below this line


def test():
    print("Counting down to blastoff:")
    countdown_to_blastoff()
    print("=====================================")


def main():
    test()


main()
