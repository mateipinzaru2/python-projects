from main import *

run_cases = [
    (Dragon("Smaug", "red"), "I am Smaug, the red dragon"),
    (Dragon("Saphira", "blue"), "I am Saphira, the blue dragon"),
]

submit_cases = run_cases + [
    (Dragon("Nefarian", "black"), "I am Nefarian, the black dragon"),
    (Dragon("Toothless", "blackish"), "I am Toothless, the blackish dragon"),
    (Dragon("Glaurung", "gold"), "I am Glaurung, the gold dragon"),
    (Dragon("Fafnir", "green"), "I am Fafnir, the green dragon"),
    (Dragon("", "colorless"), "I am , the colorless dragon"),
]


def test(input1, expected_output):
    try:
        print("---------------------------------")
        print(f"Input: {input1}")
        print(f"Expecting: {expected_output}")
        result = str(input1)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
