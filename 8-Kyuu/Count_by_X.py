#Create a function with two arguments that will return an array of the first (n) multiples of (x).

#Assume both the given number and the number of times to count will be positive numbers greater than 0.

#Return the results as an array (or list in Python, Haskell or Elixir).

def count_by(x, n):
    new = []
    another_value = x
    for number in range(n):
        new.append(x)
        x+=another_value
    return new