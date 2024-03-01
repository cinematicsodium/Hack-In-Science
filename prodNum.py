# Create a function to find the product of a random list of integers.

from random import randint

def mul(numbers: list):
    prod: int = 1
    count = 0
    for i in numbers:
        prod *= i
        count += 1
    
    formatted_integers: str = ', '.join(str(num) for num in sorted(numbers))

    print(f'Integers to multiply: {formatted_integers} (Count: {count})\n')
    print(f'Product of integers: {prod}')


listNums: list = [randint(1,25) for i in range(randint(5,20))]

mul(listNums)
