# Eratosthenovo síto

def get_numbers():
    i = 0
    while True:
        yield i
        i = i + 1

def is_divisor(a, b):
    return (b % a) == 0

def remove_multiples(n, iterable):
    return filter(lambda m: not is_divisor(n, m), iterable)

"""
>>> list(remove_multiples(2, range(20)))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""

def get_primes():
    numbers = get_numbers()
    next(numbers)
    next(numbers)
    while True:
        prime = next(numbers)
        numbers = remove_multiples(prime, numbers)
        yield prime

primes = get_primes()
for i in range(100):
    print(next(primes))

# Všechna prvočísla:
"""
for prime in get_primes():
    print(prime)
"""
