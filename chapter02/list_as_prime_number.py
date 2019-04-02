def get_prime_numbers(lower, higher):
    primes = []
    for num in range(lower, higher + 1):
        for prime in range(2, num + 1):
            is_prime = True
            for item in range(2, int(num ** 0.5) + 1):
                if num % item == 0:
                    is_prime = False
                    break

        if is_prime:
           primes.append(num)
print(get_prime_numbers(30, 30000))
