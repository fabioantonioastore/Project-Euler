CONSECUTIVE_SEQUENCE_LENGHT = 4
prime_cache = {1: False, 2: True}


def is_prime(number: int) -> bool:
    if number in prime_cache:
        return prime_cache[number]
    if number % 2 == 0:
        prime_cache[number] = False
        return False
    square_root = number ** (1 / 2)
    for i in range(3, int(square_root) + 1, 2):
        if number % i == 0:
            prime_cache[number] = False
            return False
    prime_cache[number] = True
    return True


def total_distinct_prime_factors(number: int) -> int:
    total_factors = 0
    square_root = number ** (1 / 2)
    for i in range(1, int(square_root) + 1):
        if number % i == 0:
            if is_prime(i):
                total_factors += 1
            if is_prime(number // i):
                total_factors += 1
    return total_factors


number = 1
while True:
    found = True
    for i in range(CONSECUTIVE_SEQUENCE_LENGHT):
        total_factors = total_distinct_prime_factors(number + i)
        if total_factors != CONSECUTIVE_SEQUENCE_LENGHT:
            found = False
            break
    if found:
        print(number)
        break
    number += 1
