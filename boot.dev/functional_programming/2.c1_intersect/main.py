""" boot.dev """


def get_common_formats(formats1: list[str], formats2: list[str]) -> set[str]:
    """
    Returns intersection of lists of strings as set.

    Args:
        formats1 (list[str]): first list of strings.
        formats2 (list[str]): second list of strings.

    Returns:
        set[str]: the intersection of 'formats1' and 'formats2'
    """

    return set(formats1).intersection(set(formats2))
