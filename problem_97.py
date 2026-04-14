LENGHT = 2_357_207
NUMBER = (28_433 * (2 ** 7_830_457)) + 1
LAST_DIGITS = 10


temp_number = NUMBER
result = 0
for i in range(LAST_DIGITS):
    result += (temp_number % 10) * (10 ** i)
    temp_number //= 10

print(result)
