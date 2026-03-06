alphabetic_position_cache: dict[str, int] = dict()


def alphabetic_position(letter: str) -> int:
    if letter in alphabetic_position_cache:
        return alphabetic_position_cache[letter]
    alphabetic_position_cache[letter] = ord(letter) - ord("A") + 1
    return alphabetic_position_cache[letter]


def reverse_triangular_sequence(number: int) -> float:
    return (((2 * number) + (1 / 4)) ** (1 / 2)) - (1 / 2)


def word_to_value(word: str) -> int:
    total = 0
    for letter in word:
        total += alphabetic_position(letter)
    return total


total = 0
with open("problem_42.txt", "r") as file:
    for line in file:
        for word in line.split(","):
            value = word_to_value(word[1:-1:])
            reverse = reverse_triangular_sequence(value)
            if reverse == int(reverse):
                total += 1

print(total)
