#!/usr/bin/python
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main():
    largest = 0
    for i in xrange(999):
        for j in xrange(i, 999):
            value = i*j
            if str(value) == str(value)[::-1] and value > largest:
                largest = value
                print '%s\t%s\t%s' % (i, j, largest)
    print largest

if __name__=='__main__':
    main()

