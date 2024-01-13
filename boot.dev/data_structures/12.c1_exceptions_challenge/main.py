"""
PURCHASING
You've been asked to work on the checkout flow of a popular e-commerce site.

CHALLENGE
Complete the purchase function. If the customer doesn't have enough money raise an exception with the text "not enough money". Don't handle the exception.

Otherwise, return the amount of money the customer has leftover after completing the purchase.
"""


def purchase(price, money_available):
    if money_available >= price:
        return money_available - price
    else:
        raise Exception("not enough money")
