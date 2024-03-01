# Use a lambda function to perform the following:
#   - List the numbers that are multiples of 'n' from a list of randomly generated numbers.

from secrets import randbelow

def filtered(list_input: list):
    divisor: int = int(input('\nEnter a number to find multiples of: '))
    
    list_div_multiples: list = sorted(list(filter(lambda x: x % divisor == 0, list_input)))

    print(f'\nDivisor: {divisor}')
    print(f'\nList of randomly generated numbers: {sorted(list_input)}')
    print(f'\nNumbers that are multiples of {divisor}: {list_div_multiples}\n')

rand_num_list: list = list(randbelow(1000) for i in range(20))

filtered(rand_num_list)
