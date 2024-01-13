"""
FIZZBUZZ
Fizzbuzz is a commonly overused little toy-program that comes up in entry-level interviews.

Complete the fizzbuzz function that loops over all the numbers from start to end (excluding the end value) and prints them. If the number is a multiple of 3, instead of printing the number, print "fizz". If the number is a multiple of 5, instead print "buzz". If it is a multiple of 3 and 5 then instead print "fizzbuzz".

For example:

1
2
fizz
4
buzz
fizz
7
8
...
14
fizzbuzz
16
...
"""


def fizzbuzz(start, end):
    for i in range(start, end):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


# Don't Touch Below This Line


def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()
