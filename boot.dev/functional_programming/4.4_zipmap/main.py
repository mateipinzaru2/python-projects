from collections.abc import Hashable
import sys


def zipmap(keys: list[str], values: list[str | int]) -> dict[str, str | int]:
    if len(keys) != len(values):
        raise ValueError("keys and values must have the same length")

    if len(keys) != len(set(keys)):
        raise ValueError("keys must be unique")

    for key in keys:
        if not isinstance(key, Hashable):
            raise TypeError("keys must be hashable")

    if len(keys) > sys.getrecursionlimit():
        raise RecursionError("keys length exceeds maximum recursion depth")

    if not keys:
        return {}
    else:
        return {keys[0]: values[0], **zipmap(keys[1:], values[1:])}
