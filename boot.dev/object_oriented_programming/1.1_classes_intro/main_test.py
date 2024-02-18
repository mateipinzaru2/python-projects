from main import *

run_cases = [
    (
        {"damage": 10, "attacks_per_second": 3},
        {"damage": 20, "attacks_per_second": 1},
        "soldier 1 wins",
    ),
    (
        {"damage": 50, "attacks_per_second": 1},
        {"damage": 50, "attacks_per_second": 2},
        "soldier 2 wins",
    ),
]

submit_cases = run_cases + [
    (
        {"damage": 100, "attacks_per_second": 1},
        {"damage": 1, "attacks_per_second": 200},
        "soldier 2 wins",
    ),
    (
        {"damage": 100, "attacks_per_second": 1},
        {"damage": 50, "attacks_per_second": 2},
        "both soldiers die",
    ),
    (
        {"damage": 1, "attacks_per_second": 1},
        {"damage": 2, "attacks_per_second": 1},
        "soldier 2 wins",
    ),
    (
        {"damage": 100, "attacks_per_second": 10},
        {"damage": 100, "attacks_per_second": 10},
        "both soldiers die",
    ),
    (
        {"damage": 100, "attacks_per_second": 2},
        {"damage": 50, "attacks_per_second": 4},
        "both soldiers die",
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    try:
        result = fight_soldiers(input1, input2)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
