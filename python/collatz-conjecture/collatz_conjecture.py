def steps(number: int) -> int:
    """
    User Ternary operator to solve the task.
    https://www.pythontutorial.net/python-basics/python-ternary-operator/
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0

    while number > 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        count += 1

    return count
