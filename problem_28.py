LIMIT = (10 ** 3) + 1


def calc_upper_bound(limit: int) -> int:
    return (limit - 1) // 2


def generate_sum(depth: int) -> int:
    if depth == 0:
        return 1
    max_value = (1 + (2 * depth)) ** 2
    min_value = ((1 + (2 * (depth - 1))) ** 2) + (2 * depth)
    middle_min = min_value + (2 * depth)
    middle_max = middle_min + (2 * depth)
    return max_value + min_value + middle_min + middle_max


total = 0
for i in range(calc_upper_bound(LIMIT) + 1):
    total += generate_sum(i)

print(total)
