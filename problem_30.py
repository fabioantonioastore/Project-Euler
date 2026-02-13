DIGITS = 5
LOWER_BOUND = 2


def lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def power_digits_sum(number: int, recursion: int, total: int = 0) -> int:
    if recursion == 0:
        return total
    total += (number % 10) ** DIGITS
    number //= 10
    recursion -= 1
    return power_digits_sum(number, recursion, total)


def calc_upper_bound() -> int:
    upper_bound = 99
    upper_bound_lenght = 2
    while upper_bound < power_digits_sum(upper_bound, upper_bound_lenght):
        upper_bound_lenght += 1
        upper_bound *= 10
        upper_bound += 9
    return upper_bound


total = 0
for number in range(LOWER_BOUND, calc_upper_bound() + 1):
    if number == power_digits_sum(number, lenght(number)):
        total += number

print(total)
