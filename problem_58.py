LIMIT_RATIO = 0.1
SQUARE_TOTAL_DIAGONALS = 4


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


def square_layer_primes(layer: int) -> int:
    square_lenght = 1 + (2 * layer)
    max_number = square_lenght ** 2
    total_primes = 0
    if is_prime(1 + max_number - square_lenght):
        total_primes += 1
    if is_prime(max_number - (2 * (square_lenght - 1))):
        total_primes += 1
    if is_prime(max_number - (3 * (square_lenght - 1))):
        total_primes += 1
    return total_primes


total_primes = 3
total_numbers = 5
layer = 2
while not (total_primes / total_numbers) < LIMIT_RATIO:
    total_primes += square_layer_primes(layer)
    total_numbers += SQUARE_TOTAL_DIAGONALS
    layer += 1

print(1 + (2 * (layer - 1)))
