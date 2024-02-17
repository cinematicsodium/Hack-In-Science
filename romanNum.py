def from_roman_numeral():
    """
    Converts a Roman numeral to an integer.

    Returns:
    int: The integer representation of the Roman numeral.
    """
    roman = input("Enter a roman numeral: \n")

    val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    sum = 0
    prev_val = 0

    for i in roman:
        curr_val = val[i]
        if curr_val > prev_val:
            sum += curr_val - 2 * prev_val
        else:
            sum += curr_val
        prev_val = curr_val

    print(sum)
from_roman_numeral()