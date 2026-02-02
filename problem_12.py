MAX_TOTAL_DIVISORS = 500


def generate_triangle(term: int) -> int:
    return (term * (term + 1)) // 2


def total_divisors(number: int) -> int:
    square_root = number ** (1 / 2)
    total = 0
    if square_root == int(square_root):
        total -= 1
    if number % 2 == 0:
        for i in range(1, int(square_root) + 1):
            if number % i == 0:
                total += 2
        return total
    for i in range(1, int(square_root) + 1, 2):
        if number % i == 0:
            total += 2
    return total


term = 1
while True:
    number = generate_triangle(term)
    if total_divisors(number) > MAX_TOTAL_DIVISORS:
        print(number)
        break
    term += 1
