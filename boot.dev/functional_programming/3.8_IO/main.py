def convert_case(text: str, target_format: str) -> str:
    if not text or not target_format:
        raise ValueError("No text or target format provided")

    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"Unsupported format: {target_format}")


# Don't edit below this line


def test(text, target_format):
    print(f"Converting '{text}' to {target_format}")
    try:
        result = convert_case(text, target_format)
        print(f"Got: {result}")
    except ValueError as error:
        print(f"Error: {error}")
    print("=====================================")


def main():
    test("don't yell at me", "uppercase")
    test("I really don't wanna go with you to prom sir", "lowercase")
    test("How to get good at Coding for Dummies", "titlecase")
    test("Will this work?", "garbagecase")


main()
