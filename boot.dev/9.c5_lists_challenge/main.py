"""
DOUBLE THE STRING!
An alien spaceship has landed on Earth! In an extremely realistic, and not completely fictional turn of events... the alien race speaks English, albeit a slightly modified version of English.

Our English: Hello there
Their English: HHeelllloo  tthheerree
CHALLENGE
Complete the double_string function. It takes a string as input and returns a "doubled" version, including spaces!

Example output

sentence = "hi im an alien"
print(double_string(sentence)) # "hhii  iimm  aann  aalliieenn"

TIP
You can iterate over a string as if it were a list of individual characters.
"""


def double_string(string):
    new_string = ""
    for s in string:
        new_string += s + s
    return new_string
