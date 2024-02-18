""" helper function """


def print_report(file_contents: str, filename: str):
    """
    Prints a book report to stdout.

    Args:
        file_contents: file as string
        filename: file path as string
    """

    words = file_contents.split()

    print()
    print(f"--- Begin report of {filename} ---")
    print(f"{len(words)} words found in the document")
    print()

    letters = {}
    for word in words:
        for char in word.lower():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

    sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_letters:
        if key.isalpha():
            print(f"The {key} character was found {value} times")

    print("--- End report ---")
    print()
