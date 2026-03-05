LIMIT = 10 ** 3
LAST_DIGITS_LENGHT = 10


number = 0
for i in range(1, LIMIT + 1):
    number += i ** i


def number_lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def digit(number: int, index: int, lenght: int) -> int:
    number //= 10 ** (lenght - index - 1)
    lenght -= (lenght - index - 1)
    for i in range(lenght - 1, 0, -1):
        power = 10 ** i
        multiple = number // power
        number -= multiple * power
    return number


last_digits = 0
lenght = number_lenght(number)
for i in range(LAST_DIGITS_LENGHT):
    last_digits += digit(number, lenght - i - 1, lenght) * (10 ** i)

print(last_digits)
