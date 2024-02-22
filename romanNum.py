'''
Convert a Roman numeral into an integer
(ex: MMXXIV --> 2024)
'''

from time import sleep
sleep(0.2)
print(f'\nEnter a Roman numeral to convert to an integer...\n')
sleep(1.2)
print(f'Enter "q" to exit...\n')
sleep(1.2)
print('Example:')
sleep(0.2)
print(f'Roman numeral:\t MCMXCVIII')
sleep(0.2)
print(f'Integer:\t 1998\n')
sleep(1.2)
print(f'Characters:\t I, V, X, L, C, D, M\n')
sleep(1.2)


def roman_to_int():
  print("Enter Roman numeral below:")
  input_numerals: str = str(input()).upper().strip()
  print()
  sleep(1)

  # Validate Characters
  while True:
    # Exit Check
    if input_numerals.lower() == 'q':
      print(f'Goodbye!\n')
      sleep(2)
      exit()
    # Invalid Character Check
    else:
      for i in input_numerals:
        if i.isdigit() or i not in "IVXLCDM":
          print(f'Invalid character: {i}\n'*3)
          print()
          sleep(2)
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

  print(f'{input_numerals}:\t {sum}')
  print()
  sleep(2)


while True:
  roman_to_int()
