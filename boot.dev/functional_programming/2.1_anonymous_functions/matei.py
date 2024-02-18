""" https://www.boot.dev/assignments/6efdb47f-520a-4fd9-8629-34eb69f57667 """

import json


def categorize_file(filename: str) -> str:
    """
    Categorize a file based on its extension.

    Args:
        filename: The name of the file.

    Returns:
        The category of the file.
    """

    with open(file="categories.json", encoding="utf-8") as f:
        categories: dict[str, str] = json.load(f)

    def get_category(file_ext: str) -> str:
        return categories.get(file_ext, "Unknown")

    return get_category(filename[filename.rfind(".") :])
