NUMBER = 600_851_475_143


def is_prime(number: int) -> int:
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    square_root = number ** (1 / 2)
    for i in range(3, int(square_root) + 1, 2):
        if number % i == 0:
            return False
    return True


def factors(number: int) -> list[int]:
    factors_list = [1, number]
    square_root = number ** (1 / 2)
    if number % square_root == 0:
        factors_list.append(int(square_root))
    if number % 2 == 0:
        for i in range(2, int(square_root) + 1):
            if number % i == 0:
                factors_list.append(i)
                factors_list.append(number // i)
        return factors_list
    for i in range(3, int(square_root) + 1, 2):
        if number % i == 0:
            factors_list.append(i)
            factors_list.append(number // i)
    return factors_list


for factor in sorted(factors(NUMBER), reverse=True):
    if is_prime(factor):
        print(factor)
        break
