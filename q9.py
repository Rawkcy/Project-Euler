#!/usr/bin/python
"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
    for b in xrange(1, 1000):
        if (500000-1000*b) / (1000-b) > 0:
            a = (500000-1000*b)/(1000-b)
            c = 1000 - a - b
            if c*c == a*a + b*b:
                print a*b*c

if __name__=='__main__':
    main()
