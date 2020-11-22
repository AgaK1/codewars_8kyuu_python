#Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    a = "".join([x * 2 for x in s])
    return a