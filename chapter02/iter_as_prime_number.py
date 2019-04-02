def is_prime(num):
    for item in range(2, int(math.sqrt(num)) + 1):
        if num % item == 0:
            prime = False
    return prime
    
def get_prime_numbers(lower, higher):
    for possible_prime in range(lower, higher):
        if is_prime(possible_prime):
            yield possible_prime
        yield False

for prime in get_prime_numbers(lower, higher):
    if prime:
        print(prime)
