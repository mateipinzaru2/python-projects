"""
ASSIGNMENT
At the hometown tavern in Fantasy Quest, the innkeeper offers free meals and retirement plans based on the age of his patrons. I wrote a function called check_for_meals_and_retirement that contains a loop that increments the age from a given starting_age to an ending_age exclusive. So we can leave the for loop's range as is.

In the body of the for loop, if age is less than 8 your code should print:

You qualify for free meals. You are AGE years old.

Otherwise, if age is greater than 65 you should print:

You qualify for retirement. You are AGE years old.

Where AGE is the current value of the age variable.

If neither of those conditions is true, don't do anything for that iteration of the loop.
"""


def check_for_meals_and_retirement(starting_age, ending_age):
    for age in range(starting_age, ending_age):
        if age < 8:
            print(f"You qualify for free meals. You are {age} years old.")
        elif age > 65:
            print(f"You qualify for retirement. You are {age} years old.")


# Don't edit below this line


def test(starting_age, ending_age):
    print(f"Checking from ages {starting_age} up to {ending_age}:")
    check_for_meals_and_retirement(starting_age, ending_age)
    print("=====================================")


def main():
    test(6, 10)
    test(63, 67)
    test(0, 76)


main()
