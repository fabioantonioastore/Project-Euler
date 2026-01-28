RANGE = 2 * (10 ** 6)


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


prime_sum = 2
for number in range(3, RANGE):
    if is_prime(number):
        prime_sum += number

print(prime_sum)
