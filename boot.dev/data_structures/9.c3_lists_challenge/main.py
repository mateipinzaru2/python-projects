"""
TEST SCORES
Your teacher has been manually grading tests by hand and it has been taking up all of her free time. The Bachelor isn't going to watch itself tonight.

She has asked you to write a program that compares an answer key to a student's multiple-choice answers and calculates the percentage of questions they got right.

CHALLENGE
Finish the get_test_scores function by looping over the answer_sheet and student_answers lists. Calculate and return the student's score.

For example, if these were the lists:

answer_sheet = ["A", "A", "C", "D"]
student_answers = ["A", "B", "C", "D"]

Then the percentage would be 75.00. The percentage should be a float, not an integer.
"""


def get_test_score(answer_sheet, student_answers):
    score = 0
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_answers[i]:
            score += 1
    percentage = score / len(answer_sheet) * 100
    return percentage
