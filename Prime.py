import math

def isPrime(n):
    # Check if n is 1 or 0
    if n <= 1:
        return False

    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return True

    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check from 5 to square root of n, using 6k ± 1 method
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Test the function
n = 7
if isPrime(n):
    print("true")
else:
    print("false")
