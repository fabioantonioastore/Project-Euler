LIMIT = 11
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


def lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def right_trunc(number: int) -> int:
    return number // 10


def left_trunc(number: int) -> int:
    number_lenght = lenght(number)
    power = 10 ** (number_lenght - 1)
    multiple = number // power
    return number - (multiple * power)


def is_truncatable_prime(number: int) -> bool:
    number_lenght = lenght(number)
    right_number = number
    left_number = number
    for _ in range(number_lenght):
        if not is_prime(right_number) or not is_prime(left_number):
            return False
        right_number = right_trunc(right_number)
        left_number = left_trunc(left_number)
    return True


eleven_truncatable_sum = 0
total = 0
number = 11
while total < LIMIT:
    if is_truncatable_prime(number):
        total += 1
        eleven_truncatable_sum += number
    number += 2


print(eleven_truncatable_sum)
