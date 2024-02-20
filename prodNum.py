'''
Create a function to find the product of a list of numbers
'''

from random import randint

def mul(numbers: list):
    prod: int = 1
    for i in numbers:
        prod *= i
    
    formatted_numbers: str = ', '.join(str(num) for num in sorted(numbers))

    print(f'Numbers to multiply: {formatted_numbers}')
    print(f'Product: {prod}')

listNums: list = [randint(1,25) for i in range(5)]

mul(listNums)