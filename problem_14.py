LIMIT = 10 ** 6
collatz_cache: dict[int, int] = {1: 1}


def sequence_lenght(number: int) -> int:
    if number in collatz_cache:
        return collatz_cache[number]
    if number % 2 == 0:
        next_number = number // 2
        collatz_cache[number] = 1 + sequence_lenght(next_number)
        return collatz_cache[number]
    next_number = (3 * number) + 1
    collatz_cache[number] = 1 + sequence_lenght(next_number)
    return collatz_cache[number]


longest_lenght = 0
longest_number = 0
for number in range(1, LIMIT):
    number_sequence_lenght = sequence_lenght(number)
    if number_sequence_lenght > longest_lenght:
        longest_lenght = number_sequence_lenght
        longest_number = number

print(longest_number)
