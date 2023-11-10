"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number):
    increaser = int(2)
    while increaser <= number/2:
        if number % increaser == 0:
            return False
        else:
            increaser += 1
    return True

def primes(number_of_primes):
    if not isinstance(number_of_primes, int) or number_of_primes < 1:
        raise ValueError("That wasn't an integer or not positive")
    list = []
    num = 2
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
        num += 1

    return list
