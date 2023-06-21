import collections

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

NUMBERS = [ONES, TWOS, THREES, FOURS, FIVES, SIXES]


def score(dice: list[int], category: int) -> int:

    most_common_value, most_common_count = collections.Counter(dice).most_common(1)[0]

    # ones - sixes
    if category in NUMBERS:
        return dice.count(category) * category
    
    # full house
    if category == FULL_HOUSE and set(collections.Counter(dice).values()) == {2, 3}:
        return sum(dice)
    
    # four of a kind
    if  category == FOUR_OF_A_KIND and most_common_count >= 4:
        return 4 * most_common_value
            
    # big straight
    if category == BIG_STRAIGHT and set(dice) == {2, 3, 4, 5, 6}:
        return 30
    
    # little straight
    if category == LITTLE_STRAIGHT and set(dice) == {1, 2, 3, 4, 5}:
        return 30
    
    # choice
    if category == CHOICE:
        return sum(dice)
    
    # yacht
    if category == YACHT and len(set(dice)) == 1:
        return 50

    return 0
