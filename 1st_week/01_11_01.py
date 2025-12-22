input = 20


def find_prime_list_under_number(number):
    primes = []

    for num in range(2, number + 1):
        for prime in primes:
            if prime * prime <= num and num % prime == 0:
                break
        else:
            primes.append(num)

    return primes


result = find_prime_list_under_number(input)
print(result)