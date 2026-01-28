RANGE = 10 ** 2


square_summation = ((RANGE * (RANGE + 1)) // 2) ** 2
square_sum = 0
for number in range(1, RANGE + 1):
    square_sum += number ** 2

print(square_summation - square_sum)
