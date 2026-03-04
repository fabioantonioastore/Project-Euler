KEY_LENGHT = 3
FIRST_KEY_INDEX = 0
MIDDLE_KEY_INDEX = 1


keylogs: list[str] = []
with open("problem_79.txt", "r") as file:
    for key in file:
        keylogs.append(key)


def key_analyzer(keylogs: list[str]) -> dict[int, set[int]]:
    result: dict[int, set[int]] = dict()
    for key in keylogs:
        index = FIRST_KEY_INDEX
        for digit in key[:KEY_LENGHT]:
            digit = int(digit)
            if not digit in result.keys():
                result[digit] = set()
            if index == FIRST_KEY_INDEX:
                index += 1
                continue
            if index == MIDDLE_KEY_INDEX:
                result[digit].add(int(key[FIRST_KEY_INDEX]))
                index += 1
                continue
            result[digit].add(int(key[FIRST_KEY_INDEX]))
            result[digit].add(int(key[MIDDLE_KEY_INDEX]))
            index += 1
    return result


def generate_passcode_by_keylogs(keylogs: list[str]) -> str:
    passcode = ""
    analyzer_result = key_analyzer(keylogs)
    size = 0
    for _ in range(len(analyzer_result)):
        for key in analyzer_result.keys():
            if len(analyzer_result[key]) == size:
                passcode += str(key)
                analyzer_result.pop(key)
                break
        size += 1
    return passcode


print(generate_passcode_by_keylogs(keylogs))
