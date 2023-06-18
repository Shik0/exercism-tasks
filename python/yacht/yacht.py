from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = 'yacht'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'full_hause'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'


def score(dice, category):
    
    zero = 0

    # ones - sixes
    if type(category) is int and category < 30:
        return sum([d for d in dice if d == category])
    
    # full house
    if category == 'full_hause' and 3 in Counter(dice).values():
        return sum(dice)
    
    # four of a kind
    if  category == 'four_of_a_kind':
        for key,value in Counter(dice).items():
            if value >= 4:
                return 4 * key
            
    # big straight
    if category == 'big_straight' and sum(dice) == 20:
        return 30
    
    # little straight
    if category == 'little_straight' and sum(dice) == 15:
        return 30
    
    # choice
    if category == 'choice':
        return sum(dice)
    
    # yacht
    if category == 'yacht' and len(Counter(dice)) == 1:
        return 50

    return zero
