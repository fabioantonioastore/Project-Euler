LIMIT = 10 ** 2
power_cache: dict[int, int] = {}


def power(base: int, exponent: int) -> int:
    hash_object = hash((base, exponent))
    if hash_object in power_cache:
        return power_cache[hash_object]
    if exponent == 0:
        return 1
    power_cache[hash_object] = base * power(base, exponent - 1)
    return power_cache[hash_object]


def number_lengh(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def digit(number: int, index: int, number_lenght: int) -> int:
    number //= 10 ** (number_lenght - index - 1)
    number_lenght -= number_lenght - index - 1
    for i in range(number_lenght - 1, 0, -1):
        power = 10 ** i
        multiple = number // power
        number -= multiple * power
    return number


def digital_sum(number: int) -> int:
    lenght = number_lengh(number)
    total = 0
    for i in range(lenght):
        total += digit(number, i, lenght)
    return total


max_digital_sum = 0
for a in range(1, LIMIT):
    for b in range(1, LIMIT):
        total = digital_sum(power(a, b))
        if total > max_digital_sum:
            max_digital_sum = total

print(max_digital_sum)
