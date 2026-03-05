SEQUENCE_LENGHT = 10 ** 3
fibonacci_cache = {1: 1, 2: 1}


def fibonacci(term: int) -> int:
    if term in fibonacci_cache:
        return fibonacci_cache[term]
    fibonacci_cache[term] = fibonacci(term - 1) + fibonacci(term - 2)
    return fibonacci_cache[term]


def number_lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        total += 1
        number //= 10
    return total


sequence = 1
term = 1
while number_lenght(sequence) < SEQUENCE_LENGHT:
    term += 1
    sequence = fibonacci(term)

print(term)
