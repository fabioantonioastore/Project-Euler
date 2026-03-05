prime_cache = {1: False, 2: True}


def is_prime(number: int) -> bool:
    if number in prime_cache:
        return prime_cache[number]
    square_root = int(number ** (1 / 2))
    for i in range(3, square_root + 1, 2):
        if number % i == 0:
            prime_cache[number] = False
            return False
    prime_cache[number] = True
    return True


def can_be_written(number: int) -> bool:
    for prime in range(3, number, 2):
        if not is_prime(prime):
            continue
        temp_number = number - prime
        temp_number /= 2
        if not temp_number == int(temp_number):
            continue
        square_root = temp_number ** (1 / 2)
        if not square_root == int(square_root):
            continue
        return True
    return False


number = 9
while True:
    if is_prime(number) or can_be_written(number):
        number += 2
        continue
    break

print(number)
