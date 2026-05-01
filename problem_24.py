CHARACTERS = [chr(i) for i in range(ord("0"), ord("9") + 1)]
PERMUTATION_POSITION = 10**6


def gen_permutations(item_list: list[str], permutation: str = ""):  # type: ignore
    for item in item_list:
        temp_permutation = permutation + item
        temp_set = item_list.copy()
        temp_set.remove(item)
        if len(temp_set) == 0:
            yield temp_permutation
        else:
            yield from gen_permutations(temp_set, temp_permutation)


millionth_permutation = None
index = 1
for permutation in gen_permutations(CHARACTERS):  # type: ignore
    if index == PERMUTATION_POSITION:
        millionth_permutation = permutation  # type: ignore
        break
    index += 1

print(millionth_permutation)  # type: ignore
