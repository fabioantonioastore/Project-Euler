RANGE_INDEX = 10 ** 3


def total_digits(number: int) -> int:
    total = 1
    while number // 10 > 0:
        total += 1
        number //= 10
    return total


def digit(number: int, index: int) -> int:
    number_lenght = total_digits(number)
    for _ in range(number_lenght - index - 1):
        number //= 10
    number_lenght = total_digits(number)
    if number_lenght == 1:
        return number
    for i in range(number_lenght - 1, 0, -1):
        power = 10 ** i
        multiple = number // power
        number -= multiple * power
    return number


def is_palindrome(number: int) -> bool:
    number_lenght = total_digits(number)
    steps = 0
    if number_lenght % 2 == 0:
        steps = number_lenght // 2
    else:
        steps = (number_lenght - 1) // 2
    for i in range(steps):
        if digit(number, i) != digit(number, number_lenght - i - 1):
            return False
    return True


largest_palindrome = 0
times = 0
for a in range(RANGE_INDEX - 1, 0, -1):
    for b in range(1, RANGE_INDEX - times):
        number = a * b
        if number > largest_palindrome and is_palindrome(number):
            largest_palindrome = number
    times += 1

print(largest_palindrome)
