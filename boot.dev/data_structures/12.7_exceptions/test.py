def test1():
    raise Exception("test")


# raise Exception by itself, will always raise an Exception object at runtime.


def test2():
    try:
        raise Exception("zero division")
    except ZeroDivisionError:
        print("zero")


# when the Exception is implemented in a try block, it will be caught by the first except block that matches the exception type.
# Since Exception is not a ZeroDivisionError, the first except block will not be executed.


def test3():
    try:
        raise Exception("zero division")
    except Exception:
        print("this one finally catches it")


# since the except block matches the Exception type, it will be executed.


def test4():
    try:
        raise Exception("zero division")
    except ZeroDivisionError:
        print("zero")
    except Exception:
        print("other")


# a try block can have multiple except blocks, and the first one that matches the exception type will be executed.

# test1()  # raises the Exception "test".
# test2()  # does not execute since test1() raises an Exception.
test3()  # this is the first function that catches the Exception.
# test4()  # the exception is caught here too.
