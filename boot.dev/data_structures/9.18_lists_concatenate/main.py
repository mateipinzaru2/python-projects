"""
ASSIGNMENT
Fantasy Quest allows users to keep lists of their favorite items. Your job is to finish the concatenate_favorites function. It takes three different parameters - the player's favorite_weapons, favorite_armor and favorite_items.

Create a new list that combines favorite_weapons, favorite_armor, and favorite_items in this order.
Return the list containing the combined favorites.
"""

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    favorites = favorite_weapons + favorite_armor + favorite_items
    return favorites
