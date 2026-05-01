DIGITS = [i for i in range(9, 0, -1)]


def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    square_root = number ** (1 / 2)
    for i in range(3, int(square_root) + 1, 2):
        if number % i == 0:
            return False
    return True


def gen_permutation(number_set: list[int], permutation: int = 0, lenght: int = 9):  # type: ignore
    for number in number_set:
        temp_number_set = number_set.copy()
        temp_number_set.remove(number)
        temp_permutation = (permutation * 10) + number
        temp_lenght = lenght - 1
        yield temp_permutation
        if temp_lenght == 0:
            yield temp_permutation
        else:
            yield from gen_permutation(temp_number_set, temp_permutation, temp_lenght)


def number_lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def digit(number: int, index: int, number_lenght: int) -> int:
    number //= 10 ** (number_lenght - index - 1)
    number_lenght -= number_lenght - index - 1
    for i in range(number_lenght - 1, 0, -1):
        power = 10**i
        multiple = number // power
        number -= multiple * power
    return number


def is_pandigital(number: int) -> bool:
    lenght = number_lenght(number)
    pandigital_sum = sum([i for i in range(1, lenght + 1)])
    total_sum = 0
    for i in range(lenght):
        total_sum += digit(number, i, lenght)
    return pandigital_sum == total_sum


largest_prime = 0
for permutation in gen_permutation(DIGITS):  # type: ignore
    if permutation > largest_prime and is_pandigital(permutation) and is_prime(permutation):  # type: ignore
        largest_prime = permutation  # type: ignore

print(largest_prime)  # type: ignore
