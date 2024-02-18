from main import *

run_cases = [
    (
        "John's Library",
        ["The Catcher in the Rye", "To Kill a Mockingbird", "1984"],
        ["J.D. Salinger", "Harper Lee", "George Orwell"],
        "kill",
        ["To Kill a Mockingbird"],
        "The Catcher in the Rye",
        "J.D. Salinger",
        [],
    )
]

submit_cases = run_cases + [
    (
        "Ashley's Library",
        [
            "The Great Gatsby",
            "Pride and Prejudice",
            "The Lord of the Rings",
            "Song of Six",
            "To Kill a Mockingbird",
        ],
        [
            "F. Scott Fitzgerald",
            "Jane Austen",
            "J.R.R. Tolkien",
            "Harper D Kill",
            "Harper Lee",
        ],
        "kill",
        ["Song of Six", "To Kill a Mockingbird"],
        "The Great Gatsby",
        "F. Scott Fitzgerald",
        [],
    ),
    (
        "Lane's Library",
        [
            "The Great Gatsby",
            "Pride and Prejudice",
            "The Lord of the Rings",
            "Song of Six",
            "To Kill a Mockingbird",
        ],
        [
            "F. Scott Fitzgerald",
            "Jane Austen",
            "J.R.R. Tolkien",
            "Harper D Kill",
            "Harper Lee",
        ],
        "the",
        ["The Great Gatsby", "The Lord of the Rings"],
        "Pride and Prejudice",
        "Ane Justen",
        ["Pride and Prejudice"],
    ),
]


def test(
    library_name,
    book_titles,
    book_authors,
    search_query,
    expected_search_results,
    remove_title,
    remove_author,
    expected_search_for_removed,
):
    print("---------------------------------")
    try:
        print(f"Testing Library: {library_name}")

        library = Library(library_name)
        for title, author in zip(book_titles, book_authors):
            library.add_book(Book(title, author))
            print(f"Adding book {title} by {author}")

        print(f"Searching for '{search_query}'")
        search_results = library.search_books(search_query)
        results_titles = [book.title for book in search_results]
        print(f"Expected: {expected_search_results}")
        print(f"Actual: {results_titles}")

        if results_titles != expected_search_results:
            print("Fail")
            return False

        print(f"Removing book {remove_title} by {remove_author}")
        library.remove_book(Book(remove_title, remove_author))

        print(f"Searching for '{remove_title}'")
        search_results = library.search_books(remove_title)
        results_titles = [book.title for book in search_results]
        print(f"Expected: {expected_search_for_removed}")
        print(f"Actual: {results_titles}")

        if results_titles == expected_search_for_removed:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed, failed = 0, 0
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
