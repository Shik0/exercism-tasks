def equilateral(sides):

    zero = 0

    if zero in sides:
        return False
    
    return sides[0]==sides[1]==sides[2]


def isosceles(sides):

    zero = 0

    if zero in sides or not side_length(sides):
        return False   
    
    return (sides[0]==sides[1]) or (sides[0]==sides[2]) or (sides[1]==sides[2])


def scalene(sides):

    zero = 0

    if zero in sides or not side_length(sides):
        return False

    return (sides[0]!=sides[1]) and (sides[0]!=sides[2]) and (sides[1]!=sides[2])


def side_length(sides):

    return True if (sides[0]+sides[1]>=sides[2]) and \
        (sides[0]+sides[2]>=sides[1]) and \
            (sides[2]+sides[1]>=sides[0]) else False
