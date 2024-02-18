""" boot.dev """


def remove_invalid_lines(document: str) -> str:
    """
    Iterates over string and removes all lines starting with "-".

    Args:
        document (str): the string to iterate over.

    Returns:
        str: the original string with all the filtered lines stripped.
    """

    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )
