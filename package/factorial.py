import math

def factorial(n):
    if type(n) == int:
        return math.factorial(n)
    else:
        raise Exception("Invalid Data Type")
