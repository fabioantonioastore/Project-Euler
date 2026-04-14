LENGHT_LIMIT = 50


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


def number_lenght(number: int) -> int:
    total = 1
    while True:
        number //= 10
        if number < 1:
            return total
        total += 1


def digit(number: int, index: int, lenght: int) -> int:
    number //= 10 ** (lenght - index - 1)
    lenght -= lenght - index - 1
    for i in range(lenght - 1, 0, -1):
        power = 10**i
        multiple = number // power
        number -= multiple * power
    return number


def is_palindrome(number: int, lenght: int) -> bool:
    if lenght % 2 == 0:
        for i in range(lenght // 2):
            if not digit(number, i, lenght) == digit(number, lenght - i - 1, lenght):
                return False
        return True
    for i in range((lenght - 1) // 2):
        if not digit(number, i, lenght) == digit(number, lenght - i - 1, lenght):
            return False
    return True


def reverse(number: int, lenght: int) -> int:
    reverse_number = 0
    for i in range(lenght):
        reverse_number = (reverse_number * 10) + digit(number, lenght - i - 1, lenght)
    return reverse_number


reversible_prime_squares: set[int] = set()
number = 3
while len(reversible_prime_squares) != LENGHT_LIMIT:
    if not is_prime(number):
        number += 2
        continue
    square_number = number**2
    if square_number in reversible_prime_squares:
        number += 2
        continue
    lenght = number_lenght(square_number)
    reverse_number = reverse(square_number, lenght)
    square_root_reverse_number = reverse_number ** (1 / 2)
    if not int(square_root_reverse_number) == square_root_reverse_number:
        number += 2
        continue
    if is_palindrome(square_number, lenght):
        number += 2
        continue
    if not is_prime(square_root_reverse_number):
        number += 2
        continue
    number += 2
    if not square_number in reversible_prime_squares:
        reversible_prime_squares.add(square_number)
    if not reverse_number in reversible_prime_squares:
        reversible_prime_squares.add(reverse_number)

print(sum(reversible_prime_squares))
