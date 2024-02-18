""" https://www.boot.dev/assignments/6efdb47f-520a-4fd9-8629-34eb69f57667 """


from typing import Callable


CATEGORIES: dict[str, str] = {".txt": "Text", ".docx": "Document", ".py": "Code"}


def categorize_file(filename: str) -> str:
    """
    Categorize a file based on its extension.

    Args:
        filename: The name of the file.

    Returns:
        The category of the file.
    """

    get_category: Callable[..., str] = lambda filename: CATEGORIES.get(
        filename, "Unknown"
    )

    return get_category(filename[filename.rfind(".") :])
