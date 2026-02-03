factorial_cache = {0: 1, 1: 1}


def factorial(number: int) -> int:
    if number in factorial_cache:
        return factorial_cache[number]
    factorial_cache[number] = number * factorial(number - 1)
    return factorial_cache[number]


def lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def factorial_upper_bound() -> int:
    nine_factorial = factorial(9)
    digits = 1
    while True:
        upper_bound = digits * nine_factorial
        if lenght(upper_bound) > digits:
            return upper_bound
        digits += 1


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


def digit_factorial(number: int) -> int:
    number_lenght = lenght(number)
    total = 0
    for i in range(number_lenght):
        total += factorial(digit(number, i, number_lenght))
    return total


total = 0
number = 10
for number in range(10, factorial_upper_bound()):
    if number == digit_factorial(number):
        total += number
    number += 1

print(total)
