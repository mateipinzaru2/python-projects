""" helper function """


def get_book_choice(books: list[str]) -> str:
    """
    Returns book path based on user input.

    Args:
        books: list[str], representing the books in the local 'books' folder.

    Output:
        book: str, representing the book path.
    """

    while True:
        try:
            book_choice = int(
                input("Enter the number of the book you want to choose: ")
            )
            if 1 <= book_choice <= len(books):
                return books[book_choice - 1]
            print(f"Please enter a number between 1 and {len(books)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
