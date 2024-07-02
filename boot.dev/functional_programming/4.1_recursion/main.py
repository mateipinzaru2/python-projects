def factorial_r(x: int) -> int:
    if x < 0:
        raise ValueError("x must be a non-negative integer")
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial_r(x - 1)