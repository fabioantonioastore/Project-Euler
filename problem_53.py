LIMIT = 10 ** 6
N_RANGE = 10 ** 2
factorial_cache = {0: 1, 1: 1}


def factorial(number: int) -> int:
    if number in factorial_cache:
        return factorial_cache[number]
    factorial_cache[number] = number * factorial(number - 1)
    return factorial_cache[number]


def combinatoric(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))


def total_greater(number: int) -> int:
    total = 0
    if number % 2 == 0:
        half = number // 2
        if combinatoric(number, half) > LIMIT:
            total += 1
            for r in range(half - 1, 0, -1):
                if not combinatoric(number, r) > LIMIT:
                    break
                total += 2
        return total
    half = (number - 1) // 2
    if combinatoric(number, half) > LIMIT:
        total += 2
        for r in range(half - 1, 0, -1):
            if not combinatoric(number, r) > LIMIT:
                break
            total += 2
    return total


total = 0
for n in range(1, N_RANGE + 1):
    total += total_greater(n)
    
print(total)
