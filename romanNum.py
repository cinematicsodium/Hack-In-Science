'''
Convert a Roman numeral into an integer
(ex: MMXXIV --> 2024)
'''

import time
from time import sleep

sleep(0.5)
print(f'\nEnter a Roman numeral to convert to an integer.')
print(f'\nEnter "q" to exit.\n')
sleep(0.5)
print('Example:')
sleep(0.5)
print(f'Roman numeral:\t MCMXCVIII')
sleep(0.5)
print(f'Integer:\t\t 1998')
sleep(0.5)
print(f'\nCharacters:\t\t I, V, X, L, C, D, M\n')
sleep(0.5)


def roman_to_int():

  input_numerals: str = str(input(f'Roman numeral:\t ')).upper().strip()
  sleep(1)

  # Validate Characters
  while True:
    # Exit Check
    if input_numerals.lower() == 'q':
      print('Goodbye!')
      exit()
    # Invalid Character Check
    else:
      for i in input_numerals:
        if i.isdigit() or i not in "IVXLCDM":
          print(f'Invalid character: {i}\n'*3)
          sleep(1)
          return ValueError
      break

  # Define numerical values
  val: dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

  # Convert numerals to integers
  numerical_values: list = [int(val[i]) for i in input_numerals]

  sum = 0

  x = 0
  while x < len(numerical_values):
    if x == 0:
      sum += numerical_values[x]
      x += 1
    elif numerical_values[x] > numerical_values[x - 1]:
      sum += numerical_values[x]
      sum -= 2 * numerical_values[x - 1]
      x += 1
    else:
      sum += numerical_values[x]
      x += 1

  print(f'Integer:\t\t {sum}')
  print()
  sleep(1)


while True:
  roman_to_int()
