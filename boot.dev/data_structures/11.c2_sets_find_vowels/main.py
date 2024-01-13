"""
VOWELS
You've been hired by a blogging company and they are asking you to analyze one of their recent posts to determine the number of vowels present in their paragraphs.

CHALLENGE
Complete the count_vowels function. It should take a string and return a count of the number of vowels within the given string, and a set of its unique vowels.

TIP
For this challenge, we are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions. In addition, treat uppercase and lowercase vowels as separate. For example, "A" and "a" are not the same.
"""


def count_vowels(text):
    count = 0
    output = set()
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for c in text:
        if c in vowels:
            count += 1
            output.add(c)
    return count, output
