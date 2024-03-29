"""
EVEN TEAMS
Students at the local wizarding school have been spending too much time trying to split their players up into even teams. The coach has provided you with a list of the players in the class and has asked you to write a program that will split the players into even teams.

CHALLENGE
Complete the split_players_into_teams function. Use a slice with a "step" to create two new lists from the players list:

even_team should have the players with even-numbered indexes.
odd_team should have the players with odd-numbered indexes.
Return even_team and odd_team in that order.

HINT
You might want to use a slice with a "step" value:

my_list[ start : stop : step ]
"""

def split_players_into_teams(players):
    even_team = players[0::2]
    odd_team = players[1::2]
    return even_team, odd_team
