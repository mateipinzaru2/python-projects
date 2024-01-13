from main import *

run_cases = [
    (
        (
            [
                "milk",
                "eggs",
                "cheese",
                "apples",
                "bananas",
                "lettuce",
                "cereal",
            ],
            [
                "milk",
                "oatmeal",
                "eggs",
                "cheese",
                "apples",
                "bananas",
                "carrots",
                "lettuce",
                "potatoes",
                "cereal",
                "chicken",
            ],
        ),
        (
            ["oatmeal", "carrots", "potatoes", "chicken"],
            {
                "milk": 2.5,
                "eggs": 3.25,
                "cheese": 3.5,
                "apples": 7.44,
                "bananas": 3.88,
                "lettuce": 1.12,
                "cereal": 5.99,
            },
            27.68,
        ),
    ),
]

submit_cases = run_cases + [
    (
        (
            ["milk", "bread", "lettuce", "cereal"],
            [
                "milk",
                "eggs",
                "bread",
                "cheese",
                "apples",
                "bananas",
                "carrots",
                "lettuce",
                "potatoes",
                "cereal",
                "chicken",
            ],
        ),
        (
            ["eggs", "cheese", "apples", "bananas", "carrots", "potatoes", "chicken"],
            {"milk": 2.5, "bread": 1.21, "lettuce": 1.12, "cereal": 5.99},
            10.82,
        ),
    ),
    (
        (
            [
                "milk",
                "eggs",
                "bread",
                "cheese",
                "apples",
                "bananas",
                "carrots",
                "lettuce",
                "potatoes",
                "cereal",
            ],
            ["milk", "bread", "lettuce", "cereal"],
        ),
        (
            [],
            {
                "milk": 2.50,
                "eggs": 3.25,
                "bread": 1.21,
                "cheese": 3.50,
                "apples": 7.44,
                "bananas": 3.88,
                "carrots": 3.89,
                "lettuce": 1.12,
                "potatoes": 32.21,
                "cereal": 5.99,
            },
            64.99,
        ),
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        unpurchased_items, receipt, total = calculate_total(*input1)
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False
    result = (unpurchased_items, receipt, total)
    print(f"Actual: {result}")
    if result == expected_output:
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
