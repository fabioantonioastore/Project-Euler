LIMIT = 10 ** 3
HUNDRED = len("hundred")
THOUSAND = len("thousand")
AND = len("and")
NUMBER_TO_NAME = {
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety")
}


def digit(number: int, index: int, lenght: int) -> int:
    number //= 10 ** (lenght - index - 1)
    lenght -= lenght - index - 1
    for i in range(lenght - 1, 0, -1):
        power = 10**i
        multiple = number // power
        number -= multiple * power
    return number


def number_letter_sum(number: int) -> int:
    if number == LIMIT:
        return NUMBER_TO_NAME[1] + THOUSAND
    if number in NUMBER_TO_NAME:
        return NUMBER_TO_NAME[number]
    if number < 100:
        return NUMBER_TO_NAME[digit(number, 0, 2) * 10] + NUMBER_TO_NAME[digit(number, 1, 2)]
    if number % 100 == 0:
        return NUMBER_TO_NAME[(digit(number, 0 , 3))] + HUNDRED
    return NUMBER_TO_NAME[digit(number, 0, 3)] + HUNDRED + AND + number_letter_sum(number % (10 ** 2))


total_letter_sum = 0
for number in range(1, LIMIT + 1):
    total_letter_sum += number_letter_sum(number)

print(total_letter_sum)
