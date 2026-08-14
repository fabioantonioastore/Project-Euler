cipher_text: list[int] = []
with open("problem_59.txt", "r") as file:
    for line in file.readlines():
        for byte in line.split(","):
            cipher_text.append(int(byte))

common_english_words = {
    "people", "water", "school", "mother", "friend", "family", "house", "that", "this", "have"
}


def _generate_passwords(password: str, characters: set[str]): # type: ignore
    if len(password) == 3:
        yield password
        return
    for character in characters:
        temp_characters = characters.copy()
        temp_characters.remove(character)
        yield from _generate_passwords(password=password + character, characters=temp_characters)


def generate_passwords(): # type: ignore
    characters = set(
        [chr(number) for number in range(ord("a"), ord("z") + 1)]
    )
    for character in characters:
        temp_characters = characters.copy()
        temp_characters.remove(character)
        yield from _generate_passwords(password=character, characters=temp_characters)


def decipher_text(password: str) -> str:
    text = ""
    index = 0
    for byte in cipher_text:
        text += chr(byte ^ ord(password[index]))
        index += 1
        if index == 3:
            index = 0
    return text


found = False
for password in generate_passwords(): # type: ignore
    if found:
        break
    text = decipher_text(password=password) # type: ignore
    common_word_count = 0
    for common_word in common_english_words:
        if common_word in text:
            common_word_count += 1
    if common_word_count >= 3:
        total = 0
        for character in text:
            total += ord(character)
        print(total)
        break
    