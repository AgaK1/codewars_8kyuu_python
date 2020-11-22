#Very simple, given a number, find its opposite.

def opposite(number):
    if number >= 0:
        return number*-1
    else:
        return abs(number)