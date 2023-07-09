def square_root(number: int) -> int:

    square = 1

    while square <= number:
        if number % square == 0 and square ** 2 == number:
            break
        else:
            square += 1
    
    return square