RANGE = 10 ** 6
prime_cache = {1: False, 2: True}


def is_prime(number: int) -> bool:
    if number in prime_cache:
        return prime_cache[number]
    if number % 2 == 0:
        prime_cache[number] = False
        return False
    square_root = number ** (1 / 2)
    for i in range(3, int(square_root) + 1, 2):
        if number % i == 0:
            prime_cache[number] = False
            return False
    prime_cache[number] = True
    return True


def lenght(number: int) -> int:
    total = 1
    while number // 10 > 0:
        number //= 10
        total += 1
    return total


def digit(number: int, index: int, number_lenght: int) -> int:
    for _ in range(number_lenght - index - 1, 0, -1):
        number //= 10
        number_lenght -= 1
    if number_lenght == 1:
        return number
    for i in range(number_lenght - 1, 0, -1):
        power = 10 ** i
        multiple = number // power
        number -= multiple * power
    return number


class Prime:
    def __init__(self, number: int) -> None:
        self.number_lenght = lenght(number)
        self.position: list[int] = [digit(number, i, self.number_lenght) for i in range(self.number_lenght)]
    
    def number(self) -> int:
        result = 0
        for i in range(self.number_lenght):
            result += self.position[i] * (10 ** (self.number_lenght - i - 1))
        return result

    def rotate(self) -> None:
        last_position = self.position[-1]
        self.position = self.position[0:-1:]
        self.position.insert(0, last_position)

    def is_circular_prime(self) -> bool:
        for _ in range(self.number_lenght - 1):
            self.rotate()
            if not is_prime(self.number()):
                return False
        return True
    

total = 0
for number in range(1, RANGE):
    if is_prime(number):
        prime = Prime(number)
        if prime.is_circular_prime():
            total += 1

print(total)
