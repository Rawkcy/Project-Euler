#! /usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# http://en.wikipedia.org/wiki/Prime_number#Number_of_prime_numbers_below_a_given_number

# initialize list of primes
primes = [2, 3, 5, 7]

# go up to 2 mil
for num in range(9, 2000001, 2):
  is_prime = True
  for prime in primes:
    # if it divides evenly then num is NOT prime
    if not num % prime:
      is_prime = False
      break
  if is_prime:
    primes.append(num)
print sum(primes)

