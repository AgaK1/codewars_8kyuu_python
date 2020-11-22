#Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

#if bmi <= 18.5 return "Underweight"

#if bmi <= 25.0 return "Normal"

#if bmi <= 30.0 return "Overweight"

#if bmi > 30 return "Obese"

def bmi(weight, height):
    if weight/height**2 <= 18.5:
        message = "Underweight"
    elif weight/height**2 <= 25.0:
        message = "Normal"
    elif weight/height**2 <= 30.0:
        message = "Overweight"
    else:
        message = "Obese"
    return(message)