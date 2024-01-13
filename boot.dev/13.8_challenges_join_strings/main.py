"""
JOIN STRINGS
Write a function called join_strings() that concatenates all of its string inputs end-to-end, in order, and adds a comma between them.

join_strings(['hello', 'my', 'friend'])
# 'hello,my,friend'

Note that you don't want a comma at the end or the beginning of the final string!
"""


# elegant solution:
def join_strings(strings):
    return ",".join(strings)


# savage solution:
# def join_strings(strings):
#     output = ""
#     for i, s in enumerate(strings):
#         if i == len(strings) - 1:
#             output += s
#         else:
#             output += s + ","
#     return output
