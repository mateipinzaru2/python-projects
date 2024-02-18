# GET EDGES
Remember that with normal "units" we were checking if their (x/y) **point** was within a rectangle (the Dragon's breath) to see if they were hit by the fire. With a dragon, because they're so big, we're going to check if the dragon's body (a rectangle) is within the fire (also a rectangle still). The image below contains an example of fire breath hitting a dragon.

![dragon](dragon.png)

## ASSIGNMENT
In the next assignment, we'll be writing the overlap method itself. First, let's set up some helper methods.

Write the following methods, what they do should be self-explanatory given their names.

- `get_left_x()`
- `get_right_x()`
- `get_top_y()`
- `get_bottom_y()`

Remember that `x1` OR `x2` could be the "left x" based on its value on the Cartesian plane. The same goes for the `y` values. You may find Python's built-in [min](https://docs.python.org/3/library/functions.html#min) and [max](https://docs.python.org/3/library/functions.html#max) functions useful if you'd rather not use the comparison operators.