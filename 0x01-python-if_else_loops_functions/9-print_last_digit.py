def print_last_digit(number):
    if number < 0:
        return (10 - (number % 10))
    return number % 10
