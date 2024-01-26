"""
LOCAL LIBRARY
A new library just opened in a small town near you! They reached out to you asking for help building a system to keep track of all the books in the library!

CHALLENGE
Complete the Library and Book classes.

BOOK CLASS
__INIT__(SELF, TITLE, AUTHOR)
Set .title and .author to the values of the parameters.

LIBRARY CLASS
Add the following methods.

__INIT__(SELF, NAME)
Initialize a .name member variable to the value of the name parameter. Create a .books member initialized to an empty list.

ADD_BOOK(SELF, BOOK)
Add the book to the books instance variable by appending it to the end of the list.

REMOVE_BOOK(SELF, BOOK)
If the book's title and author match a library book's title and author, the remove_book method should remove that library book from the list.

SEARCH_BOOKS(SELF, SEARCH_STRING)
For every book in the library check if the search_string is contained in the title or author field (case insensitive). Return a list of all books that match the search string, ordered in the same order as they were added to the library.
"""


class Book:
    # pylint: disable=too-few-public-methods
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return (
                self.title.lower() == other.title.lower()
                and self.author.lower() == other.author.lower()
            )
        return False


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_books(self, search_string):
        return [
            book
            for book in self.books
            if search_string.lower() in book.author.lower()
            or search_string.lower() in book.title.lower()
        ]
