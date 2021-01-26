# Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1 (in C#, N might be less then 1).

# Replace certain values however if any of the following conditions are met:

# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# Method calling example:

# fizzbuzz(3) -->  [1, 2, "Fizz"]


def fizzbuzz(n):
    values = []
    for num in range(1, n + 1):
        if (num % 3 == 0) and (num % 5 == 0):
            values.append("FizzBuzz")
        elif num % 3 == 0:
            values.append("Fizz")
        elif num % 5 == 0:
            values.append("Buzz")
        else:
            values.append(num)
    return values
