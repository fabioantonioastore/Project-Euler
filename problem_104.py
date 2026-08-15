fibonacci_cache = {1: 1, 2: 1}


def number_lenght(number: int) -> int:
    total = 0
    while number > 0:
        number //= 10
        total += 1
    return total


def get_digits(number: int, index: int, lenght: int = 9) -> int:
    if index == 0:
        return number // (10 ** (lenght - 1))
    number %= 10 ** (lenght - 1)
    return get_digits(number=number, index=index - 1, lenght=lenght - 1)


def get_last_nine_digits(number: int) -> set[int]:
    last_nine_digits = number % (10 ** 9)
    digits: set[int] = set()
    for i in range(9):
        digits.add(get_digits(number=last_nine_digits, index=i, lenght=9))
    return digits


def get_first_nine_digits(number: int) -> set[int]:
    lenght = number_lenght(number=number)
    digits: set[int] = set()
    for i in range(9):
        digits.add(get_digits(number=number, index=i, lenght=lenght))
    return digits


def is_pandigital(numbers: set[int]) -> bool:
    return numbers == {1, 2, 3, 4, 5, 6, 7, 8, 9}


def fibonacci(n: int) -> int:
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    fibonacci_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_cache[n]


k = 541
while True:
    number = fibonacci(n=k)
    last_nine_digits = get_last_nine_digits(number=number)
    if is_pandigital(numbers=last_nine_digits):
        first_nine_digits = get_first_nine_digits(number=number)
        if is_pandigital(numbers=first_nine_digits):
            print(k)
            break
    k += 1
