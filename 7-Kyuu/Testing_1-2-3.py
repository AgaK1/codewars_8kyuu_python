# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples:

# number([]) # => []
# number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]

def number(lines):
    new = []
    if not lines:
        return []
    else:
        for count, lines in enumerate(lines, start=1):
            new.append(str(count) + ": " + lines)
        return new
