def is_evenly_divisible(number: int) -> bool:
    for divisor in range(20, 10, -1):
        if number % divisor != 0:
            return False
    return True


number = 2540
while True:
    if is_evenly_divisible(number):
        print(number)
        break
    number += 20
