LIMIT = 28123


def proper_divisors(number: int) -> set[int]:
    divisors: set[int] = {1}
    square_root = int(number ** (1 / 2))
    if number % 2 == 0:
        for i in range(2, square_root + 1):
            if number % i == 0:
                divisors.add(number // i)
                divisors.add(i)
        return divisors
    for i in range(3, square_root + 1, 2):
        if number % i == 0:
            divisors.add(number // i)
            divisors.add(i)
    return divisors


def is_abundant(number: int) -> bool:
    divisors = proper_divisors(number=number)
    return sum(divisors) > number


abundants: set[int] = set()
for i in range(2, LIMIT):
    if is_abundant(i):
        abundants.add(i)

abundant_sum_numbers: set[int] = set()
for a in abundants:
    for b in abundants:
        result = a + b
        if result > LIMIT:
            break
        abundant_sum_numbers.add(result)

not_abundant_sum = 0
for i in range(1, LIMIT + 1):
    if i in abundant_sum_numbers:
        continue
    not_abundant_sum += i

print(not_abundant_sum)
