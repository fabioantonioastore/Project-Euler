RANGE_INDEX = 552 * (10 ** 3)
odd_square_sum = 0


for square in range(1, RANGE_INDEX + 1, 2):
    odd_square_sum += square ** 2

print(odd_square_sum)
