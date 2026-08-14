prime_cache = set([1, 2])


def is_prime(n: int) -> bool:
    if n in prime_cache:
        return True
    square_root = int(n ** (1 / 2))
    for i in range(3, square_root + 1, 2):
        if n % i == 0:
            return False
    prime_cache.add(n)
    return True


def formula(n: int, a: int, b: int) -> int:
    return (n ** 2) + (a * n) + b 


def get_total_primes_from_formula(a: int, b: int) -> int:
    n = 0
    total = 0
    while True:
        number = formula(n=n, a=a, b=b)
        if number < 0:
            return total
        if is_prime(n=number):
            total += 1
            n += 1
            continue
        return total


max_total_primes = 0
coeficient = 0
for a in range(1_000):
    for b in range(1_001):
        total = get_total_primes_from_formula(a=a, b=b)
        if total > max_total_primes:
            max_total_primes = total
            coeficient = a * b
        total = get_total_primes_from_formula(a=a, b=-b)
        if total > max_total_primes:
            max_total_primes = total
            coeficient = a * (-b)
        total = get_total_primes_from_formula(a=-a, b=b)
        if total > max_total_primes:
            max_total_primes = total
            coeficient = (-a) * b
        total = get_total_primes_from_formula(a=-a, b=-b)
        if total > max_total_primes:
            max_total_primes = total
            coeficient = (-a) * (-b)

print(coeficient)
