"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for item in items:

        if str(item) not in frequencies.keys():
            frequencies.update({str(item): 1})
        else:
            frequencies.update({str(item): frequencies[str(item)] + 1})

    return frequencies

frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4'])