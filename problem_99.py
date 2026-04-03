log10_cache: dict[int, float] = dict()


def log10(number: int) -> float:
    if number in log10_cache:
        return log10_cache[number]
    if number <= 0:
        log10_cache[number] = 0
        return 0
    lower_bound = 0
    upper_bound = number
    iterations = 100
    if number < 1:
        lower_bound -= iterations
        upper_bound = 0
    tolerance = 10 ** (-10)
    for _ in range(iterations):
        middle = (lower_bound + upper_bound) / 2
        temp = 10 ** (middle % 1)
        for _ in range(int(middle)):
            temp *= 10
        if abs(temp - number) < tolerance:
            log10_cache[number] = middle
            return middle
        if temp < number:
            lower_bound = middle
            continue
        upper_bound = middle
    log10_cache[number] = (lower_bound + upper_bound) / 2
    return log10_cache[number]


greatest_line = 0
with open("problem_99.txt", "r") as file:
    line = 0
    greatest_base = 1
    greatest_exponent = 1
    for number in file.readlines():
        line += 1
        base_and_exponent = number.split(",")
        base = int(base_and_exponent[0])
        exponent = int(base_and_exponent[1])
        if (exponent * log10(base)) > (greatest_exponent * log10(greatest_base)):
            greatest_line = line
            greatest_base = base
            greatest_exponent = exponent

print(greatest_line)
