def reverse_triangle(n: int) -> float:
    square_root = ((8 * n) + 1) ** (1 / 2)
    return (square_root - 1) / 2


def reverse_square(n: int) -> float:
    return n ** (1 / 2)


def reverse_pentagonal(n: int) -> float:
    square_root = ((24 * n) + 1) ** (1 / 2)
    return (square_root + 1) / 6


def reverse_hexagonal(n: int) -> float:
    square_root = ((8 * n) + 1) ** (1 / 2)
    return (square_root + 1) / 4


def reverse_heptagonal(n: int) -> float:
    square_root = ((40 * n) + 9) ** (1 / 2)
    return (square_root + 3) / 10


def reverse_octagonal(n: int) -> float:
    square_root = ((3 * n) + 1) ** (1 / 2)
    return (square_root + 1) / 3


def is_triangle(n: int) -> bool:
    reverse = reverse_triangle(n)
    return reverse == int(reverse)


def is_square(n: int) -> bool:
    reverse = reverse_square(n)
    return reverse == int(reverse)


def is_pentagonal(n: int) -> bool:
    reverse = reverse_pentagonal(n)
    return reverse == int(reverse)


def is_hexagonal(n: int) -> bool:
    reverse = reverse_hexagonal(n)
    return reverse == int(reverse)


def is_heptagonal(n: int) -> bool:
    reverse = reverse_heptagonal(n)
    return reverse == int(reverse)


def is_octagonal(n: int) -> bool:
    reverse = reverse_octagonal(n)
    return reverse == int(reverse)


def is_valid(n: int, function: int) -> bool:
    if function == 3:
        return is_triangle(n=n)
    if function == 4:
        return is_square(n=n)
    if function == 5:
        return is_pentagonal(n=n)
    if function == 6:
        return is_hexagonal(n=n)
    if function == 7:
        return is_heptagonal(n=n)
    if function == 8:
        return is_octagonal(n=n)
    return False


def map_figurate_numbers_by_first_two_digits() -> dict[int, dict[int, set[int]]]:
    figurates: dict[int, dict[int, set[int]]] = {}
    for i in range(10, 100):
        figurates[i] = {3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        for j in range(100):
            temp = i * 100
            temp += j
            if is_hexagonal(n=temp):
                figurates[i][6].add(temp)
                figurates[i][3].add(temp)
            elif is_triangle(n=temp):
                figurates[i][3].add(temp)
            if is_square(n=temp):
                figurates[i][4].add(temp)
            if is_pentagonal(n=temp):
                figurates[i][5].add(temp)
            if is_heptagonal(n=temp):
                figurates[i][7].add(temp)
            if is_octagonal(n=temp):
                figurates[i][8].add(temp)
    return figurates


def is_four_digit_number(n: int) -> bool:
    return (n // 1_000) != 0


def get_last_two_digits(n: int) -> int:
    return (n % (1_000)) % (100)


def get_first_two_digits(n: int) -> int:
    return ((n // 1_000) * 10) + ((n % 1_000) // 100)


def _get_ordered_set(ordered_set: list[int], remains: set[int], items: dict[int, dict[int, set[int]]]):  # type: ignore
    if len(remains) == 0:
        yield ordered_set
    if len(remains) == 1:
        number = (get_last_two_digits(n=ordered_set[-1]) * 100) + get_first_two_digits(
            n=ordered_set[0]
        )
        if is_four_digit_number(n=number) and is_valid(
            n=number, function=remains.pop()
        ):
            ordered_set.append(number)
            yield ordered_set
            return
        else:
            yield None
            return
    last_two_digits = get_last_two_digits(n=ordered_set[-1])
    if last_two_digits < 10:
        yield None
        return None
    for remain in remains:
        numbers = items[last_two_digits][remain]
        if len(numbers) == 0:
            yield None
            continue
        for number in numbers:
            temp_remains = remains.copy()
            temp_remains.remove(remain)
            temp_ordered_set = ordered_set.copy()
            temp_ordered_set.append(number)
            yield from _get_ordered_set(
                ordered_set=temp_ordered_set, remains=temp_remains, items=items
            )


def get_ordered_set():  # type: ignore
    items = map_figurate_numbers_by_first_two_digits()
    for i in range(10, 100):
        for number in items[i][8]:
            yield from _get_ordered_set(
                ordered_set=[number], remains={7, 6, 5, 4, 3}, items=items
            )


for ordered_set in get_ordered_set():  # type: ignore
    if ordered_set is not None:
        print(sum(ordered_set))  # type: ignore
        break
