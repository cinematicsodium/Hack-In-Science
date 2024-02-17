from collections import Counter
from string import ascii_lowercase as Letters

with open('words.txt', 'r') as File:
    text = File.read()
    c = Counter(text)

    # Count all lowercase in File
    for i in Letters:
        if c[i] != 0:
            frequency = c[i] / sum(c.values())
            print(f'{i}: [{frequency:.2f}]')