## algorithm to find all prime numbers less than the given number n.
def sieve(limit):
    primes = [True] * (limit+1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5)+1):
        if primes[i]:
            for j in range(i**2, limit+1, i):
                primes[j] = False
    return [i for i in range(2, limit+1) if primes[i]]