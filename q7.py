#!/usr/bin/python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(num):
    factor = num - 1
    while num % factor != 0:
        factor -= 1
    if factor == 1:
        return True
    return False

def next_prime(prime):
    while not is_prime(prime):
        prime += 1
    return True, prime

def main():
    primes = [2]
    while len(primes) < 10001:
        found, prime = next_prime(primes[-1] + 1)
        if found:
            primes.append(prime)
    print '%s prime #: %s' % (len(primes), primes[-1])


if __name__=='__main__':
    main()

