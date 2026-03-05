NUMBER = 2 ** (10 ** 3)


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


lenght = number_lenght(NUMBER)
total = 0
for i in range(lenght):
    total += digit(NUMBER, i, lenght)

print(total)
