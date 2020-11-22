#The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).


def cockroach_speed(s):
    return 0 if s == 0 else int(s * 27.7777778)
