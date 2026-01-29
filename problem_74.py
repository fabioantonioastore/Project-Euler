LIMIT = 10 ** 6
SIZE = 60
factorial_cache = {0: 1, 1: 1}
factorial_digits_cache: dict[int, int] = {}


def factorial(number: int) -> int:
    if number in factorial_cache:
        return factorial_cache[number]
    factorial_cache[number] = number * factorial(number - 1)
    return factorial_cache[number]


def digits(number: int) -> int:
    total = 1
    while number // 10 > 0:
        total += 1
        number //= 10
    return total


def digit(number: int, index: int) -> int:
    number_lenght = digits(number)
    for _ in range(number_lenght - index - 1):
        number //= 10
    number_lenght = digits(number)
    if number_lenght == 1:
        return number
    for i in range(number_lenght - 1, 0, -1):
        power = 10 ** i
        multiple = number // power
        number -= multiple * power
    return number


def factorial_digits(number: int) -> int:
    if number in factorial_digits_cache:
        return factorial_digits_cache[number]
    new_number = 0
    for i in range(digits(number)):
        new_number += factorial(digit(number, i))
    factorial_digits_cache[number] = new_number
    return new_number


def create_chain(number: int) -> set[int]:
    chain = {number}
    number = factorial_digits(number)
    while not number in chain:
        chain.add(number)
        number = factorial_digits(number)
    return chain


total = 0
for number in range(1, LIMIT):
    chain = create_chain(number)
    if len(chain) == SIZE:
        total += 1

print(total)
