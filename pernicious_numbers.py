# Pernicious Numbers
# A pernicious number is a positive integer whose binary digit sum (or Hamming weight) is a prime number.

import math

# Iterate through the range of numbers
for i in range(654321, 654421):
    
    # Convert the number to binary
    decBin = bin(i)[2:]
    
    # Count the number of '1' digits in the binary representation
    count = decBin.count('1')
                
    # Check if the count is a prime number
    def isPrime(n):
        return n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))
    
    if isPrime(count):
        print(int(decBin, 2), decBin, count, sep='\t')
