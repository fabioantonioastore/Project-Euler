def number_lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def digit(number: int, index: int, lenght: int) -> int:
    for _ in range(lenght - index - 1, 0, -1):
        number //= 10
        lenght -= 1
    if lenght == 1:
        return number
    for i in range(lenght - 1, 0, -1):
        power = 10 ** i
        multiple = number // power
        number -= multiple * power
    return number


def number_to_set(number: int, lenght: int) -> set[int]:
    digits: set[int] = set()
    for i in range(lenght):
        digits.add(digit(number, i, lenght))
    return digits


def is_same_digits(x: int) -> bool:
    x5 = 5 * x
    x2 = 2 * x
    x2_lenght = number_lenght(x2)
    if x2_lenght != number_lenght(x5):
        return False
    x2_set = number_to_set(x2, x2_lenght)
    if (
        not x2_set == number_to_set(3 * x, x2_lenght) or
        not x2_set == number_to_set(4 * x, x2_lenght) or
        not x2_set == number_to_set(x5, x2_lenght)
    ):
        return False
    return True


x = 1
while not is_same_digits(x):
    x += 1

print(x)
