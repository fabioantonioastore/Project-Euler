def get_digit(number: int, index: int, lenght: int) -> int:
    if index == 0:
        return number // (10 ** (lenght - 1))
    number %= 10 ** (lenght - 1)
    return get_digit(number=number, index=index - 1, lenght=lenght - 1)


def number_lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


lenght = 0
number = 0
integer = 1
product = 1
while lenght <= 10**6:
    integer_lenght = number_lenght(number=integer)
    number = (number * (10**integer_lenght)) + integer
    integer += 1
    lenght += integer_lenght
    if (
        lenght == 1
        or lenght == 10**2
        or lenght == 10**3
        or lenght == 10**4
        or lenght == 10**5
        or lenght == 10**6
    ):
        product *= get_digit(
            number=integer - 1, index=(integer_lenght - 1), lenght=integer_lenght
        )
        continue
    if lenght - integer_lenght < 10**2 and lenght > 10**2:
        count = lenght - (10**2)
        product *= get_digit(
            number=integer - 1,
            index=(integer_lenght - count - 1),
            lenght=integer_lenght,
        )
        continue
    if lenght - integer_lenght < 10**3 and lenght > 10**3:
        count = lenght - (10**3)
        product *= get_digit(
            number=integer - 1,
            index=(integer_lenght - count - 1),
            lenght=integer_lenght,
        )
        continue
    if lenght - integer_lenght < 10**4 and lenght > 10**4:
        count = lenght - (10**4)
        product *= get_digit(
            number=integer - 1,
            index=(integer_lenght - count - 1),
            lenght=integer_lenght,
        )
        continue
    if lenght - integer_lenght < 10**5 and lenght > 10**5:
        count = lenght - (10**5)
        product *= get_digit(
            number=integer - 1,
            index=(integer_lenght - count - 1),
            lenght=integer_lenght,
        )
        continue
    if lenght - integer_lenght < 10**6 and lenght > 10**6:
        count = lenght - (10**6)
        product *= get_digit(
            number=integer - 1,
            index=(integer_lenght - count - 1),
            lenght=integer_lenght,
        )

print(product)
