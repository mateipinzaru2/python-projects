from main import *

run_cases = [
    ("Merlin", "Madame Mim", ["cast_fireball"], [25, 35], None),
    ("Madame Mim", "Merlin", ["cast_fireball", "drink_mana_potion"], [65, 35], None),
]

submit_cases = run_cases + [
    ("Gandalf", "Saruman", ["drink_mana_potion", "cast_fireball"], [65, 35], None),
    (
        "Merlin",
        "Madame Mim",
        ["cast_fireball", "cast_fireball", "cast_fireball"],
        [None, None],
        "Merlin cannot cast fireball",
    ),
    (
        "Merlin",
        "Madame Mim",
        ["cast_fireball", "cast_fireball", "drink_mana_potion", "cast_fireball"],
        [25, -25],
        None,
    ),
]


def test(caster_name, target_name, actions, expected_output, expected_err):
    try:
        print("---------------------------------")
        print(f"Caster: {caster_name}")
        print(f"Target: {target_name}")
        print(f"Caster actions: {actions}")
        caster = Wizard(caster_name)
        target = Wizard(target_name)

        for action in actions:
            if action == "cast_fireball":
                fireball_result = caster.cast_fireball(target)
                print(fireball_result)
                if fireball_result != f"{caster.name} casts fireball at {target.name}":
                    print(f"Expected: {caster.name} casts fireball at {target.name}")
                    print("Fail")
                    return False

            elif action == "drink_mana_potion":
                caster.drink_mana_potion()

        if expected_err:
            print(f"Expected Exception: {expected_err}")
            print("Actual: no exception raised")
            print("Fail")
            return False

        actual_output = [caster.get_mana(), target.get_health()]
        print(
            f"Expected: {caster_name} mana: {expected_output[0]}, {target_name} health: {expected_output[1]}"
        )
        print(
            f"Actual: {caster_name} mana: {actual_output[0]}, {target_name} health: {actual_output[1]}"
        )
        if actual_output == expected_output:
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        if str(e) == expected_err:
            print(f"Expected: {expected_err}")
            print(f"Actual: {str(e)}")
            print("Pass")
            return True
        print(f"Fail: {e}")
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
