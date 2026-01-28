RANGE = (10 ** 3) + 1


found = False
for c in range(1, RANGE - 3):
    if found:
        break
    for b in range(1, RANGE - c - 1):
        if b >= c:
            break
        if found:
            break
        for a in range(1, RANGE - c - b):
            if a >= b:
                break
            if a + b + c == 1_000 and (a ** 2) + (b ** 2) == (c ** 2):
                print(a * b * c)
                found = True
                break
