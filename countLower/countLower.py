'''
Count all lowercase letters in a file and print the frequency of each letter.
'''

from collections import Counter
from string import ascii_lowercase as Letters

with open('words.txt', 'r') as File:
    text = File.read()
    c = Counter(text)

    for i in Letters:
        if c[i] != 0:
            frequency = c[i] / sum(c.values())
            print(f'{i}: [{frequency:.2f}]')