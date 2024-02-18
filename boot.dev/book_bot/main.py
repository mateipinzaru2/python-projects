""" boot.dev book bot project """

import os
from src.get_book_choice import get_book_choice
from src.read_file import read_file
from src.print_report import print_report


def main():
    """
    Presents the user the option to choose any book from the local 'books' folder.
    After the user chooses a book, the program prints a book report to stdout.
    """

    try:
        books = os.listdir("books")
    except FileNotFoundError:
        print("The 'books' directory could not be found.")
        return

    if not books:
        print("No books found in the 'books' directory.")
        return

    for i, book in enumerate(books, start=1):
        print(f"{i}. {book}")

    filename = get_book_choice(books)
    file_contents = read_file(filename)

    if file_contents is not None:
        print_report(file_contents, filename)


if __name__ == "__main__":
    main()
