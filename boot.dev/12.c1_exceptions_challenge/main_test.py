from main import *

run_cases = [
    (10.00, 20.00, 10.00),
    (30.00, 20.00, "not enough money"),
]

submit_cases = run_cases + [
    (15.10, 15.10, 0.0),
    (1430.00, 69.00, "not enough money"),
    (7.50, 7.50, 0.0),
    (100.00, 99.99, "not enough money"),
    (0.0, 0.0, 0.0),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * price: {input1}")
    print(f" * money_available: {input2}")
    print(f"Expecting: {expected_output}")
    try:
        result = purchase(input1, input2)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
    except Exception as e:
        print(f"Actual Exception: {str(e)}")
        if str(e) == expected_output:
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
