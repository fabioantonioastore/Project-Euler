RANGE = 100
powers: set[int] = set()


for a in range(2, RANGE + 1):
    for b in range(2, RANGE + 1):
        powers.add(a ** b)

print(len(powers))
