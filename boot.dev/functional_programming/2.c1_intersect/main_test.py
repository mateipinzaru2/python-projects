from main import *

run_cases = [
    (["PDF", "DOCX", "TXT"], ["PDF", "MD", "HTML"], set(["PDF"])),
    (
        ["PDF", "DOCX", "TXT", "HTML"],
        ["PDF", "MD", "HTML", "TXT"],
        set(["PDF", "TXT", "HTML"]),
    ),
]

submit_cases = run_cases + [
    (["TXT"], ["TXT"], set(["TXT"])),
    (["PDF", "DOCX", "TXT"], ["JPEG", "GIF", "PNG"], set()),
    (["PDF", "DOCX"], ["DOCX", "PDF", "TXT"], set(["PDF", "DOCX"])),
]


def test(formats1, formats2, expected_output):
    print("---------------------------------")
    print(f"Formats for Software 1: {formats1}")
    print(f"Formats for Software 2: {formats2}")
    print(f"Expecting: {expected_output}")
    result = get_common_formats(formats1, formats2)
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
