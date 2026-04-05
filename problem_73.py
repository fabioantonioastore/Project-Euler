LIMIT = 12 * (10**3)
LOWER_BOUND_RATIO = 1 / 3
UPPER_BOUND_RATIO = 1 / 2


def hcf(a: int, b: int) -> int:
    if b == 0:
        return a
    return hcf(b, a % b)


total = 0
for n in range(1, LIMIT):
    if n % 2 == 0:
        for d in range(n + 1, LIMIT + 1, 2):
            division_result = n / d
            if (
                division_result > LOWER_BOUND_RATIO
                and division_result < UPPER_BOUND_RATIO
            ):
                if hcf(n, d) == 1:
                    total += 1
        continue
    for d in range(n + 1, LIMIT + 1):
        division_result = n / d
        if division_result > LOWER_BOUND_RATIO and division_result < UPPER_BOUND_RATIO:
            if hcf(n, d) == 1:
                total += 1

print(total)
