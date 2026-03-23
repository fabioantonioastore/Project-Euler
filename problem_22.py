alphabetic_position_cache: dict[str, int] = {}


def alphabetic_position(letter: str) -> int:
    if letter in alphabetic_position_cache:
        return alphabetic_position_cache[letter]
    alphabetic_position_cache[letter] = ord(letter) - ord("A") + 1
    return alphabetic_position_cache[letter]


def alphabetic_score(name: str) -> int:
    score = 0
    for letter in name:
        score += alphabetic_position(letter)
    return score


def name_score(name: str, position: int) -> int:
    return alphabetic_score(name) * position


names: list[str] = []
with open("problem_22.txt", "r") as file:
    for line in file:
        for name in line.split(","):
            name = name.removeprefix("\"")
            name = name.removesuffix("\"")
            names.append(name)


names.sort()
total_score = 0
for i in range(len(names)):
    total_score += name_score(names[i], i + 1)

print(total_score)
