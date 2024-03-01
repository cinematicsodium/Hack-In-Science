# Adam Number: A number for which the reverse of its square is the square of its reverse.
# Example using the number 13:
#     The reverse of 13 is 31
#     The square of 13 is 169
#     The square of 31 is 961
#     The reverse of 169 is 961
#     169 == 961, reversed
#     13 is an Adam number

def check_adam_number(n):
    nSquared = int(n) ** 2
    nReversed: str = str(n)[::-1]
    nReversedSquared = int(nReversed) ** 2
    flip_reverseSquared = int(str(nReversedSquared)[::-1])
    return nSquared == flip_reverseSquared