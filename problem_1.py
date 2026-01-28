RANGE_INDEX = 10 ** 3
multiples_sum = 0

for n in range(1, RANGE_INDEX):
    if n % 3 == 0 or n % 5 == 0:
        multiples_sum += n

print(multiples_sum)
