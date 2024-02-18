""" boot.dev """


def change_bullet_style(document: str) -> str:
    """
    Parses string and replaces the first line character if it's equal to "-".

    Args:
        document (str): string to be parsed.

    Returns:
        str: original string with "-" replaced by "*" if it's the first character in the line.
    """

    return "\n".join(map(convert_line, document.split("\n")))


# Don't edit below this line


def convert_line(line: str) -> str:
    """
    Replaces "-" with "*" if it's the first character in the line.

    Args:
        line (str): input string to check and replace the first character.

    Returns:
        str: original line with "-" replaced by "*" if found.
    """

    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
