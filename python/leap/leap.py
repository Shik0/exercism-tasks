def leap_year(year):

    leaped = False

    # if (not (year % 4) or not (year // 400)) and year % 100:
    #     leaped = True

    if (not year % 4) and (not year % 100 and not year % 400):
        leaped = True

    return leaped
