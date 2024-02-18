""" https://www.boot.dev/assignments/8c6cafe9-5cb2-40b7-a42d-5cfe75f6e15c """


def get_median_font_size(font_sizes: list[int]) -> int | float | None:
    """
    Calculate the median font size from a list of font sizes.

    Args:
        font_sizes: List of font sizes.

    Returns:
        median_font_size: int | float | None.

    Raises:
        TypeError: If font_sizes is not a list.
        ValueError: If elements of font_sizes are not integers or floats.
    """

    if not isinstance(font_sizes, list):
        raise TypeError("font_sizes must be a list")

    if not all(isinstance(size, (int, float)) for size in font_sizes):
        raise ValueError("All font sizes must be integers or floats")

    sorted_font_sizes = sorted(font_sizes)

    if not sorted_font_sizes:
        return None

    length = len(sorted_font_sizes)
    mid = (length - 1) // 2

    if length % 2:
        return sorted_font_sizes[mid]
    return (sorted_font_sizes[mid] + sorted_font_sizes[mid + 1]) / 2
