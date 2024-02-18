from main import *

run_cases = [
    ("Merlin", 45, 65),
    ("Madame Mim", 45, 65),
]

submit_cases = run_cases + [
    ("Gandalf", 45, 65),
    ("Dumbledore", 45, 65),
    ("Aragorn", 45, 65),
    ("Frodo", 45, 65),
    ("Harry", 45, 65),
    ("Ron", 45, 65),
    ("Hermione", 45, 65),
]


def test(input1, expected_output1, expected_output2):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Wizard name: {input1}")
    print(f"Expecting: Mana - {expected_output1}, Health - {expected_output2}")
    wizard = Wizard(input1)
    result1 = wizard.get_mana()
    result2 = wizard.get_health()
    print(f"Actual: Mana - {result1}, Health - {result2}")
    if result1 == expected_output1 and result2 == expected_output2:
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
