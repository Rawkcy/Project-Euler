#!/usr/bin/python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
largest_factor = 1

def largest_prime_factor(num):

    def div_loop(num, factor):
        global largest_factor
        while num % factor == 0:
            largest_factor = factor
            num = num/factor
        return num

    num = div_loop(num, 2) # rid of even factors
    # rid of odd factors
    factor = 3
    while num > 1:
        num = div_loop(num, factor)
        factor += 2
    return largest_factor

def main():
    num = 600851475143
    print largest_prime_factor(num)

if __name__=='__main__':
    main()

