from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'full_hause'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 30
CHOICE = 'choice'


def score(dice, category):
    
    if type(category) is int and category < 30:
        return sum([d for d in dice if d == category])
    
    if category == 'full_hause' and len(Counter(dice) == 2):
        return sum(dice)
    
    if category == 'four_of_a_kind' and 

    return None
