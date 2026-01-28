TERM_FACTORIAL = 10 ** 2
factorial_cache = {1: 1}


def factorial(term: int) -> int:
    if term in factorial_cache:
        return factorial_cache[term]
    factorial_cache[term] = term * factorial(term - 1)
    return factorial_cache[term]


def digits(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
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


factorial_value = factorial(100)
factorial_digit_sum = 0
for i in range(digits(factorial_value)):
    factorial_digit_sum += digit(factorial_value, i)

print(factorial_digit_sum)
