#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

def summation(num):
    result = 0
    count = 1

    while count <= num:
        result += count
        count += 1

    return result