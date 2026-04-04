LIMIT = 10 ** 3


def is_a_solution(p: int, c: int) -> bool:
    m = c - p
    k = (p * (p - (2 * c))) / 2
    b = (m / 2) + ((((m * m) / 4) - k) ** (1 / 2))
    if isinstance(b, complex):
        return False
    return b == int(b)


def total_perimeter_solutions(perimeter: int) -> int:
    total_solutions = 0
    for c in range(3, perimeter - 2):
        if is_a_solution(perimeter, c):
            total_solutions += 1
    return total_solutions


solutions: dict[int, int] = {}
for p in range(3, LIMIT + 1):
    solutions[p] = total_perimeter_solutions(p)

max_solution = (1, 1)
for key, value in solutions.items():
    if value > max_solution[1]:
        max_solution = (key, value)

print(max_solution[0])
