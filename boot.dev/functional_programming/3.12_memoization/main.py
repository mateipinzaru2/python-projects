def word_count_memo(document: str, memos: dict[str, int]) -> tuple[int, dict[str, int]]:
    """
    Count the number of words in a document that do not start with a symbol.
    Cache the result in a local dictionary for future reference.

    Args:
        document: A string of text to count words in.
        memos: A dictionary to store previously computed word counts.

    Returns:
        A tuple containing the word count and an updated copy of the memos dictionary.
    """

    local_memos = memos.copy()
    words = [word for word in document.split() if word[0].isalnum()]
    if document not in local_memos:
        local_memos[document] = len(words)
    return local_memos.get(document, len(words)), local_memos


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
