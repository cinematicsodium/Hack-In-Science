# Create a function called `missing_card` that, when provided with a card game, 
# identifies and returns the name of the single missing card.
# The card game is presented as a string containing space-separated card names.
# Each card is denoted by its color and value. Colors are limited to {"S", "H", "D", "C"}, 
# and values are chosen from {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A,"} 
# resulting in a total of 52 possible combinations.
# Assume the input will always consist of 51 cards, and the task is to determine and return the missing one.

def missing_card(cards):
    colors: set = {"S", "H", "D", "C"}
    values: set = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
    allCards: list = [c+v for c in colors for v in values]
    missing: list = [card for card in allCards if card not in cards.split()]
    result = missing[0] if len(missing) == 1 else ', '.join(i for i in missing)
    print(result)

missing_card("S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK")