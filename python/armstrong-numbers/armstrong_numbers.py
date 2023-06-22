def is_armstrong_number(number):

    exp_digit = len(str(number))

    return number == sum(int(digit) ** exp_digit for digit in str(number))
