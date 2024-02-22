'''
Collatz sequence: A mathematical sequence that starts with a positive integer.

    1. If the current number is even, divide it by 2.
    2. If the current number is odd, multiply it by 3 and add 1.
    3. Repeat steps 1 and 2 with the new number obtained.
    4. Keep repeating these steps until you reach the number 1.

Example: 6
    6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It is believed that no matter which positive integer you start with, 
the sequence will always reach 1. However, this has not been proven 
yet and remains an unsolved problem in mathematics.
'''
from time import sleep
def collatz_length():
    while True:
        sleep(0.5)
        n: str = str(input('\nEnter a number from 1 - 256 to display its Collatz sequence ("q" to quit): '))
        if n.lower() == 'q':
            sleep(1)
            print(f'\nGoodbye!\n')
            sleep(1)
            exit()
        elif not n.isdigit() or int(n) > 256:
            sleep(1)
            print(f'\nInvalid Entry. Please try again.')
            continue
        else:
            break
    n = int(n)
    collatzSeq = [n]
    lenSequence = 0
    startNum = n
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        lenSequence += 1
        collatzSeq.append(n)
    collatzSeq = ', '.join(str(i) for i in collatzSeq)
    sleep(1)
    print(f'\nNumber:\t\t{startNum}')
    sleep(0.5)
    print(f'Sequence:\t{collatzSeq}')
    sleep(0.5)
    print(f'Seq. Count:\t{lenSequence} numbers\n')

while True:
    collatz_length()