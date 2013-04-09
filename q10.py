#!/usr/bin/python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

# http://en.wikipedia.org/wiki/Prime_number#Number_of_prime_numbers_below_a_given_number
"""

import math

def is_prime(num):
  divisor = 2
  while divisor <= int(math.sqrt(num)):
    if num % divisor == 0:
      return False
    divisor += 1
  return True

def main():
  primes = []
  for i in xrange(2, 2000000):
    if is_prime(i):
      print i
      primes.append(i)
  print sum(primes)


if __name__=='__main__':
  main()
