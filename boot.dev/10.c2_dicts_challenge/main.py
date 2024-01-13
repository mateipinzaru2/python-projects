"""
TOTAL SCORE
A website that tracks basketball scores and stats is having trouble with its data. The first-half score and second-half score are stored in separate dictionaries, making it difficult for them to parse the overall score. They have asked you to help them write a program that merges the two dictionaries and another function that calculates the total score.

CHALLENGE
Complete the merge and total_score functions.

The merge function accepts two score dictionaries as input and returns a single merged dictionary that contains all of the keys and values from the input dictionaries.

The total_score function should take a single score dictionary as input and return the total score calculated from the values of that dictionary. Take a look at the test suite near the top of the file for the names of keys to expect. If no points were scored, the function should return 0.

Don't forget: you can always add print() statements to your code so that you can debug your code before submitting! Print out values of variables to see what's going on, and question your assumptions about what you think is happening.

EXAMPLE OF DEBUGGING WITH PRINT STATEMENTS
def total_score(score_dict):
    print(f"score_dict: {score_dict}")
    for key in score_dict:
        print(f"key: {key}")

You would then run your code and manually inspect the output to see what's going on. You can always remove the print statements when you're done debugging if you want.
"""


def merge(dict1, dict2):
    merged = {}
    for k1, k2 in zip(dict1, dict2):
        merged[k1] = dict1[k1]
        merged[k2] = dict2[k2]
    return merged


def total_score(score_dict):
    total = 0
    for k in score_dict:
        total += score_dict[k]
    return total
