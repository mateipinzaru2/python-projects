from main import *

run_cases = [
    ("Merlin", ["get_fireballed", "drink_mana_potion"], [35, 85]),
    ("Merlin", ["drink_mana_potion", "get_fireballed", "drink_mana_potion"], [35, 125]),
]

submit_cases = run_cases + [
    ("Madame Mim", ["get_fireballed", "get_fireballed"], [5, 45]),
    ("Madame Mim", ["get_fireballed", "get_fireballed", "get_fireballed"], [-25, 45]),
    ("Madame Mim", ["drink_mana_potion", "drink_mana_potion"], [65, 125]),
    ("Madame Mim", ["get_fireballed", "drink_mana_potion", "get_fireballed"], [5, 85]),
]


def test(name, actions, expected_values):
    print("---------------------------------")
    try:
        print(f"Testing Wizard {name} with Actions: {actions}")
        wizard = Wizard(name)

        for action in actions:
            if action == "get_fireballed":
                print(f"{wizard.name} gets fireballed")
                wizard.get_fireballed()
            elif action == "drink_mana_potion":
                print(f"{wizard.name} drinks a mana potion")
                wizard.drink_mana_potion()

        actual_values = [wizard.get_health(), wizard.get_mana()]
        print(f"Expected Final Health and Mana: {expected_values}")
        print(f"Actual Final Health and Mana: {actual_values}")

        if actual_values == expected_values:
            print("Pass")
            return True
        else:
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
