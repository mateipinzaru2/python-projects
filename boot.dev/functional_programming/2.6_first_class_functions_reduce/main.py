""" boot.dev """

import functools


def accumulate(doc: str, sentence: str) -> str:
    """
    Adds two strings together.

    Args:
        doc (str): document at the end of which to add the sentence.
        sentence (str): string to be added at the end of doc.

    Returns:
        str: doc + sentence
    """

    if not doc:
        return sentence

    return doc + ". " + sentence


def accumulate_first_sentences(sentences: list[str], n: int) -> str:
    """
    Adds sentences together separated by ". ".

    Args:
        sentences (list[str]): sentences to be added together.
        n (int): number of sentences to be added together. Must be <= len(sentences).

    Returns:
        str: sentences added together, returned as single string.
    """

    if not sentences or n < 1:
        return ""

    return functools.reduce(accumulate, sentences[:n], "") + "."
