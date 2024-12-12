#!/usr/bin/python3
""" Prime Game File
"""


def isWinner(x, nums):
    """ isWinner Function
    """
    if x < 1 or not nums:
        return None

    # Function to calculate prime numbers up to max number in nums
    def prime_sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]

    max_num = max(nums)
    primes = prime_sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = 0
        used_primes = set()
        for prime in primes:
            if prime > n:
                break
            if prime not in used_primes:
                primes_count += 1
                for multiple in range(prime, n + 1, prime):
                    used_primes.add(multiple)

        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
