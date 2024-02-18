""" helper function """

from typing import Optional


def read_file(filename: str) -> Optional[str]:
    """
    Returns the content of a file as string.

    Args:
        filename: str, representing the book path.

    Returns:
        str: the file as string

    Raises:
        FileNotFoundError: if book is not found
    """

    try:
        with open(file=f"books/{filename}", mode="r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"The file 'books/{filename}' could not be found.")
        return None
