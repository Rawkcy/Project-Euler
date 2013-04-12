#!/usr/bin/python
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(num):
    divisors = []
    for divisor in xrange(1, num):
        if num % divisor == 0:
            divisors.append(divisor)
    return sum(divisors)

def main():
    amicable_pairs = []
    for i in xrange(1, 10000):
        pair = d(i)
        if i == d(pair) and i != pair:
            if i not in amicable_pairs:
                amicable_pairs.append(i)
            if pair not in amicable_pairs:
                amicable_pairs.append(pair)
    print sum(amicable_pairs)


if __name__=='__main__':
    main()

