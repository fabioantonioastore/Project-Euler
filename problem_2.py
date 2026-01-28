MAX_FIBONACCI_VALUE = 4 * (10 ** 6)
fibonacci_cache = {0: 1, 1: 1}


def fibonacci(term: int) -> int:
    if term in fibonacci_cache:
        return fibonacci_cache[term]
    fibonacci_cache[term] = fibonacci(term - 1) + fibonacci(term - 2)
    return fibonacci_cache[term]


fibonacci_sum = 0
term = 1
while True:
    result = fibonacci(term)
    if result >= MAX_FIBONACCI_VALUE:
        break
    if result % 2 == 0:
        fibonacci_sum += result
    term += 1

print(fibonacci_sum)
