def is_prime(num):
    for digit in range(2, int(num ** 0.5) + 1):
        if num % digit == 0:
            return False
    else:
        return True
