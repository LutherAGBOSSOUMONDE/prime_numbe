def is_prime(number):
    if number == 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False

    return True
