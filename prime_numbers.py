# Check if a number is prime; return True or False.

import math 

def isPrime(n):
        return n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))

n = 60

if isPrime(n):
    print(f'{n} is prime.')
else:
    print(f'{n} is not prime.')