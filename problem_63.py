def number_lenght(number: int) -> int:
    total = 0
    while number > 0:
        number //= 10
        total += 1
    return total


def nine_exponent_upper_bound() -> int:
    e = 1
    while number_lenght(9 ** e) == e:
        e += 1
    return e - 1


total = 0
for i in range(1, 10):
    for j in range(1, nine_exponent_upper_bound() + 1):
        if number_lenght(i ** j) == j:
            total += 1
            continue
        break

print(total)
