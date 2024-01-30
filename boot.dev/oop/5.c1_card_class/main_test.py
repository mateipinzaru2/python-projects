from main import *

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

run_cases = [
    ("Ace", "Hearts", "Queen", "Diamonds", False, True),
    ("2", "Spades", "2", "Diamonds", False, True),
]

submit_cases = run_cases + [
    ("Ace", "Spades", "Ace", "Spades", True, False),
    ("3", "Clubs", "7", "Clubs", False, False),
    ("King", "Spades", "King", "Hearts", False, True),
    ("Queen", "Diamonds", "Queen", "Clubs", False, True),
    ("10", "Hearts", "10", "Hearts", True, False),
]


def test(input1, input2, input3, input4, expected_output_eq, expected_output_gt):
    print("---------------------------------")
    print(f"Inputs: {input1} of {input2}, {input3} of {input4}")
    print(
        f"Expecting: {expected_output_eq} for equality, {expected_output_gt} for greater than"
    )
    card1 = Card(input1, input2)
    card2 = Card(input3, input4)
    result_eq = card1 == card2
    result_gt = card1 > card2
    print(f"Actual: {result_eq} for equality, {result_gt} for greater than")
    if result_eq == expected_output_eq and result_gt == expected_output_gt:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
