LIMIT_RANGE = 10**4
MAX_INTERATIONS = 49
lychrel_cache: dict[int, bool] = {}


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


def is_palindrome(number: int) -> bool:
    lenght = number_lenght(number)
    if lenght % 2 == 0:
        for i in range(lenght // 2):
            if not digit(number, i, lenght) == digit(number, lenght - i - 1, lenght):
                return False
        return True
    for i in range((lenght - 1) // 2):
        if not digit(number, i, lenght) == digit(number, lenght - i - 1, lenght):
            return False
    return True


def reverse_number(number: int) -> int:
    lenght = number_lenght(number)
    reversed_number = 0
    for i in range(lenght):
        reversed_index = lenght - i - 1
        reversed_number += digit(number, reversed_index, lenght) * (10**reversed_index)
    return reversed_number


def is_lychrel(number: int, interations: int = 0) -> bool:
    if number in lychrel_cache:
        return lychrel_cache[number]
    if interations < MAX_INTERATIONS:
        temp_number = number + reverse_number(number)
        if is_palindrome(temp_number):
            lychrel_cache[number] = False
            return False
        lychrel_cache[number] = is_lychrel(temp_number, interations + 1)
        return lychrel_cache[number]
    lychrel_cache[number] = True
    return True


total_lychrel = 0
for number in range(LIMIT_RANGE):
    if is_lychrel(number):
        total_lychrel += 1

print(total_lychrel)
