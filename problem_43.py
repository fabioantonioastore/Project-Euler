NUMBER_LENGHT = 10


def _pandigital_number_generator(number: int, digits: set[int]):  # type: ignore
    if len(digits) == 0:
        yield number
        return
    number *= 10
    for digit in digits:
        temp_digits = digits.copy()
        temp_digits.remove(digit)
        temp_number = number + digit
        yield from _pandigital_number_generator(number=temp_number, digits=temp_digits)


def pandigital_number_generator():  # type: ignore
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for digit in digits:
        temp_digits = digits.copy()
        temp_digits.remove(digit)
        temp_digits.add(0)
        yield from _pandigital_number_generator(digit, temp_digits)


def get_digit(number: int, index: int, lenght: int = NUMBER_LENGHT) -> int:
    if index == 0:
        return number // (10 ** (lenght - 1))
    number %= 10 ** (lenght - 1)
    return get_digit(number=number, index=index - 1, lenght=lenght - 1)


def is_by_two(number: int) -> bool:
    return get_digit(number, index=3) % 2 == 0


def is_by_three(number: int) -> bool:
    return (
        get_digit(number=number, index=2)
        + get_digit(number=number, index=3)
        + get_digit(number=number, index=4)
    ) % 3 == 0


def is_by_five(number: int) -> bool:
    return get_digit(number=number, index=5) % 5 == 0


def is_by_seven(number: int) -> bool:
    temp_number = get_digit(number=number, index=4) * 10
    temp_number = (temp_number + get_digit(number=number, index=5)) * 10
    temp_number += get_digit(number=number, index=6)
    return temp_number % 7 == 0


def is_by_eleven(number: int) -> bool:
    temp_number = get_digit(number=number, index=5) * 10
    temp_number = (temp_number + get_digit(number=number, index=6)) * 10
    temp_number += get_digit(number=number, index=7)
    return temp_number % 11 == 0


def is_by_thirteen(number: int) -> bool:
    temp_number = get_digit(number=number, index=6) * 10
    temp_number = (temp_number + get_digit(number=number, index=7)) * 10
    temp_number += get_digit(number=number, index=8)
    return temp_number % 13 == 0


def is_by_seventeen(number: int) -> bool:
    temp_number = get_digit(number=number, index=7) * 10
    temp_number = (temp_number + get_digit(number=number, index=8)) * 10
    temp_number += get_digit(number=number, index=9)
    return temp_number % 17 == 0


def is_sub_string_divisibility(number: int) -> bool:
    return (
        is_by_two(number=number)
        and is_by_three(number=number)
        and is_by_five(number=number)
        and is_by_seven(number=number)
        and is_by_eleven(number=number)
        and is_by_thirteen(number=number)
        and is_by_seventeen(number=number)
    )


total_sum = 0
for number in pandigital_number_generator():  # type: ignore
    if is_sub_string_divisibility(number=number):  # type: ignore
        total_sum += number  # type: ignore

print(total_sum)  # type: ignore
