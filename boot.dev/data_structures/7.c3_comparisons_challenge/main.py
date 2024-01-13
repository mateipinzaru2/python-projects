"""
GAS MILEAGE
There isn't a gas station between Tyler's house and his work. He is trying to figure out if his car has enough gas to get him to work and back home.

CHALLENGE
Complete the has_enough_gas function.

Do some Pythonic math to determine how many gallons are needed for Tyler to get to work AND make it back home after he gets off work. Assign the result to a gallons_needed variable.

Return True if there are at least enough gallons in the tank based on the gallons_needed variable, and False otherwise.
"""

def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
    gallons_needed = miles_one_way / miles_per_gallon * 2
    if gallons_in_car >= gallons_needed:
        return True
    return False
