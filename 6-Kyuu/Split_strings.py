# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    pairs = []
    for char in range(len(s)):
        if len(s) % 2 != 0:
            s = s + "_"
            print(s)
        if char % 2 == 0:
            pairs.append(s[char:char + 2])
    return pairs
