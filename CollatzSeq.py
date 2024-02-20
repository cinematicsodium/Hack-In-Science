'''
Collatz sequence: A mathematical sequence that starts with a positive integer.

    1. If the current number is even, divide it by 2.
    2. If the current number is odd, multiply it by 3 and add 1.
    3. Repeat steps 1 and 2 with the new number obtained.
    4. Keep repeating these steps until you reach the number 1.

Example: 6
    6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It is believed that no matter which positive integer you start with, the sequence will always reach 1. However, this has not been proven yet and remains an unsolved problem in mathematics.
'''

def collatz_length():
    n: int = int(input('\nEnter a number to display its Collatz sequence: '))
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

    print(f'\n Number:\t{startNum} \n Sequence:\t{collatzSeq} \n Count:\t\t{lenSequence} numbers\n')


collatz_length()

