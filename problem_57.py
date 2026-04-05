LIMIT = 10**3


def _square_root_expansion(
    expansion: int, fraction: tuple[int, int] = (1, 2)
) -> tuple[int, int]:
    for i in range(expansion, 0, -1):
        fraction = (fraction[1], (2 * fraction[1]) + fraction[0])
        if i == 1:
            return (fraction[1] + fraction[0], fraction[1])
    return fraction


def square_root_expansion(expansion: int) -> tuple[int, int]:
    if expansion == 0:
        return (3, 2)
    return _square_root_expansion(expansion)


def number_lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


total = 0
for e in range(LIMIT):
    expansion = square_root_expansion(e)
    if number_lenght(expansion[0]) > number_lenght(expansion[1]):
        total += 1

print(total)
