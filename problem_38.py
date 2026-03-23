MAX_LENGHT = 9
INTEGER_UPPER_BOUND = 10**4


def is_unique(string: str) -> bool:
    characters: set[str] = set()
    for character in string:
        characters.add(character)
    return len(string) == len(characters)


def number_lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


interger = 1
max_pandigital = 0
for i in range(1, INTEGER_UPPER_BOUND):
    pandigital = str(interger)
    n = 2
    while True:
        pandigital += str(interger * n)
        if len(pandigital) > MAX_LENGHT:
            break
        if not is_unique(pandigital):
            break
        if len(pandigital) == MAX_LENGHT:
            if int(pandigital) > max_pandigital:
                max_pandigital = int(pandigital)
                break
        n += 1
    interger += 2

print(max_pandigital)
