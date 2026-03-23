LIMIT = 10 ** 6


def binary_form(number: int) -> int:
    return int(str(bin(number))[2::])


def number_lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def digit(number: int, index: int, lenght: int) -> int:
    number //= 10 ** (lenght - index - 1)
    lenght -= (lenght - index - 1)
    for i in range(lenght - 1, 0, -1):
        power = 10 ** i
        multiple = number // power
        number -= multiple * power
    return number


def is_palindrome(number: int) -> bool:
    lenght = number_lenght(number)
    if lenght % 2 == 0:
        for i in range(lenght // 2):
            if not digit(number, i, lenght) == digit(number, lenght - i - 1, lenght):
                return False
        return True
    for i in range((lenght - 1) // 2):
        if not digit(number, i, lenght) == digit(number, lenght - i - 1, lenght):
            return False
    return True


def is_double_base_palindrome(number: int) -> bool:
    return is_palindrome(number) and is_palindrome(binary_form(number))


total_sum = 0
for number in range(LIMIT):
    if is_double_base_palindrome(number):
        total_sum += number

print(total_sum)
