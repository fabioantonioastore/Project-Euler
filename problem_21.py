RANGE = 10 ** 4
amicable_transform_cache = {220: 284}


def proper_divisors(number: int) -> list[int]:
    divisors = [1]
    square_root = number ** (1 / 2)
    if number % 2 == 0:
        for i in range(2, int(square_root) + 1):
            if number % i == 0:
                divisors.append(i)
                divisors.append(number // i)
        return divisors
    for i in range(3, int(square_root) + 1, 2):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number // i)
    return divisors


def amicable_transform(number: int) -> int:
    if number in amicable_transform_cache:
        return amicable_transform_cache[number]
    new_amicable = 0
    for divisor in proper_divisors(number):
        new_amicable += divisor
    amicable_transform_cache[number] = new_amicable
    return new_amicable


def is_amicable(number: int) -> bool:
    amicable = amicable_transform(number)
    if number == amicable:
        return False
    return number == amicable_transform(amicable)


amicable_sum = 0
for number in range(1, RANGE):
    if is_amicable(number):
        amicable_sum += number

print(amicable_sum)
