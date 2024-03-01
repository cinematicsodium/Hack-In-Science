# Let Σ1={(,)} be an alphabet consisting of the left and right parentheses. 
# Given word, u, over Σ1, let D1(u) be the number of occurrences of the 
# left parentheses in u minus the number of occurrences of the right 
# parentheses in u.
# -------------------------------------------------------------------------
# A word u over Σ1 is said to be a word of well-balanced parentheses, if:
#     1. D1(u)=0, and 
#     2. D1(v)≥0 for any prefix v of u.
# -------------------------------------------------------------------------
# Example:  True: (())          False: ))())(()     True: ()
#           False: )))(()())(() True: ))(()(        False: ()(()))()()
# -------------------------------------------------------------------------
import random

def is_a_dyck_word(word: str) -> bool:
    
    def two_unique_chars(word):
        return len(set(word)) == 2
    
    def char_delta_zero(word):
        wordSet = set(word)
        delta = []
        for char in wordSet:
            delta.append(word.count(char))
        return delta[0] - delta[1] == 0
    
    def prefix_zero_plus(word):
        initChar = word[0]
        count = 0
        for i in range(len(word)):
            if word[i] == initChar:
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count >= 0
    
    if len(word) == 0:
        return True
    if two_unique_chars(word):
        if char_delta_zero(word):
            if prefix_zero_plus(word):
                return True
    return False

# Dyck Word Generator
def dyck_word_generator(n: int) -> list:
    # Create a random Dyck word
    def random_dyck_word():
        chars = ['1', '0']
        dyckWord = ''
        for j in range(random.randint(2, 12)):
            dyckWord += random.choice(chars)
        return dyckWord

    # Generate n Dyck words
    dyckWords = []
    half = round(n/2)
    while len(dyckWords) < half:
        word = random_dyck_word()
        if word not in dyckWords:
            dyckWords.append(word)
        else:
            continue
    while len(dyckWords) < n:
        j = random.randint(0, len(dyckWords)-1)
        word = random_dyck_word()
        if is_a_dyck_word(word) and word not in dyckWords:
            dyckWords.insert(j, word)
        else:
            continue
    return dyckWords

# Test the dyck_word_generator function
dyck_word_count = 12
dyckWords = dyck_word_generator(dyck_word_count)
print(f'Dyck words: {dyckWords}')
for i in dyckWords:
    print(f'{is_a_dyck_word(i)}: {i}')