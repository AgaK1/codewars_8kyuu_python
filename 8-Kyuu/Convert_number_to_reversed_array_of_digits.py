#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.


def digitize(n):
    n_reversed = str(n)[::-1]
    return list(map(int, str(n_reversed)))