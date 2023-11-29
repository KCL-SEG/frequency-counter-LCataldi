"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    frequency_dict = {}

    for item in items:

        if str(item) not in frequency_dict.keys():
            frequency_dict.update({str(item): 1})
        else:
            frequency_dict.update({str(item): frequency_dict[str(item)] + 1})

    return frequencies