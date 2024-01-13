"""
TEST SCORES 2
The teacher you helped earlier was so satisfied with how easy your program made it for her to grade her student's tests that she wants to take this further! She wants a more flexible program that can grade all of her student's tests.

CHALLENGE
Complete the get_test_score function. It should calculate a report that describes the percentage of multiple-choice answers a student got right on their test.

INPUTS
answer_sheet: A list of the correct multiple-choice answers
student_answers: A list where the first index is the name of the student, but the rest of the list consists of the student's multiple-choice answers.
OUTPUT
The function should return 2 values:

name: a string
percentage: a float
e.g.

return name, percentage
"""


def get_test_score(answer_sheet, student_answers):
    name = student_answers[0]
    answers = student_answers[1:]
    score = 0
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == answers[i]:
            score += 1
    percentage = score / len(answer_sheet) * 100
    return name, percentage
