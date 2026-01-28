LIMIT = 10 ** 6
amicable_transform_cache = {220: 284}
amicable_chain_cache: dict[int, list[int] | None] = {12496: [14288, 15472, 14536, 14264]}


def proper_divisors(number: int) -> list[int]:
    divisors = [1]
    square_root = number ** (1 / 2)
    if number % 2 == 0:
        for i in range(2, int(square_root) + 1):
            if number % i == 0:
                divisors.append(i)
                divisors.append(number // i)
        return divisors
    for i in range(3, int(square_root) + 1, 2):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number // i)
    return divisors


def amicable_transform(number: int) -> int:
    if number in amicable_transform_cache:
        return amicable_transform_cache[number]
    new_amicable = 0
    for divisor in proper_divisors(number):
        new_amicable += divisor
    amicable_transform_cache[number] = new_amicable
    return new_amicable
        

def create_chain(number: int) -> set[int] | None:
    chain = {number}
    amicable = amicable_transform(number)
    while number != amicable:
        if amicable > LIMIT or amicable == 1 or amicable in chain:
            return None
        chain.add(amicable)
        amicable = amicable_transform(amicable)
    return chain


longest_chain: set[int] = set()
for i in range(1, LIMIT + 1):
    chain = create_chain(i)
    if chain and len(chain) > len(longest_chain):
        longest_chain = chain

print(min(longest_chain))
