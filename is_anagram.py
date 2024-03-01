# Write a simple function named "is_anagram" that takes two strings and returns a boolean value.
# The function should return True if the letters of one word are a rearrangement of the letters of the other, and False otherwise.
# Superfluous (or missing) spaces, quotes, dashes, etc., are allowed; for example, "funeral" is an anagram of "real fun."
# Capitalized letters are equivalent to lowercase letters; for instance, "Madam Curie" is an anagram of "Radium came."
# Diacritics of any language are ignored; for example, "crâné" is an anagram of "crane."

def is_anagram(left, right):
    import unicodedata as ud
    
    def normalize_lower_sort(text):
        categories = ['Lu', 'Ll']
        text = list(ud.normalize('NFKD', text))
        text = [i for i in text if ud.category(i) in categories]
        text = [i.lower() for i in text]
        text.sort()
        text = ''.join(text)
        return text
    
    if normalize_lower_sort(left) == normalize_lower_sort(right):
        print(f'\n{left} and {right} are anagrams.\n')
    else:
        print(f'\n{left} and {right} are NOT anagrams.\n')

is_anagram('Él le regañó', 'a leer en gol')
is_anagram('Dip Flonky', 'Pink Floyd')