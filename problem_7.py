LIMIT = (10 ** 4) + 1


def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    square_root = number ** (1 / 2)
    for i in range(3, int(square_root) + 1, 2):
        if number % i == 0:
            return False
    return True


total_primes = 1
number = 3
while True:
    if is_prime(number):
        total_primes += 1
        if total_primes == LIMIT:
            break
    number += 2

print(number)
