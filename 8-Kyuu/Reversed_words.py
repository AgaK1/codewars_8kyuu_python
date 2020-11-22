#Complete the solution so that it reverses all of the words within the string passed in.


def reverseWords(s):
    w = s.split(" ")
    return " ".join(w[::-1])