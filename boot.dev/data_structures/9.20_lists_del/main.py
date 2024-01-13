"""
ASSIGNMENT
In Fantasy Quest there is a list of strongholds on the map that players can visit to defeat powerful bosses. Let's update the trim_strongholds function to:

Delete the first stronghold from the list
Delete the last two strongholds from the list
Return the new trimmed-down list
"""

def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
    return strongholds