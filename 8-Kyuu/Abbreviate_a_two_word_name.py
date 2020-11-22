# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# Patrick Feeney => P.F

def abbrev_name(name):
    first_name = name[0].upper()
    last_name_index = name.find(" ") + 1
    last_name = name[last_name_index].upper()
    return first_name + "." + last_name