"""
AREA SUM
Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}

The function will calculate the area of each rectangle, then sum them all up and return the result.
"""


def area_sum(rectangles):
    if not isinstance(rectangles, list) or not all(
        isinstance(r, dict) for r in rectangles
    ):
        raise TypeError("Input must be a list of dictionaries")
    area = 0
    for r in rectangles:
        if r.keys() >= {"height", "width"}:
            area += r["height"] * r["width"]
    return area
