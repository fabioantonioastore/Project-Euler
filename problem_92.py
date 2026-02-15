RANGE = 10 ** 7
square_cache = {1: 1}
chain_cache = {1: 1, 89: 89}


def square(number: int) -> int:
    if number in square_cache:
        return square_cache[number]
    square_cache[number] = number ** 2
    return square_cache[number]


def lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def digit(number: int, index: int, number_lenght: int) -> int:
    number //= 10 ** (number_lenght - index - 1)
    number_lenght -= (number_lenght - index - 1)
    for i in range(number_lenght - 1, 0, -1):
        power = 10 ** i
        multiple = number // power
        number -= multiple * power
    return number


def square_digits(number: int) -> int:
    number_lenght = lenght(number)
    new_number = 0
    for i in range(number_lenght):
        new_number += square(digit(number, i, number_lenght))
    return new_number


def calc_upper_bound() -> int:
    return square(9) * lenght(RANGE)


def chain_end_number(number: int, upper_bound: int) -> int:
    start_number = number
    if start_number <= upper_bound:
        chain = [number]
        while True:
            if number in chain_cache:
                result = chain_cache[number]
                for chain_number in chain:
                    chain_cache[chain_number] = result
                return result
            chain.append(number)
            number = square_digits(number)
    while True:
        if number <= upper_bound and number in chain_cache:
            return chain_cache[number]
        number = square_digits(number)


total = 0
upper_bound = calc_upper_bound()
for number in range(1, RANGE):
    if chain_end_number(number, upper_bound) == 89:
        total += 1

print(total)
