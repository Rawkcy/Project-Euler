#! /usr/bin/env python

def divisible(num, divisor):
    # check if the number is divisible by 1 to 20
    if divisor <= 20:
        # if divisible
        if num%divisor == 0 and divisible(num, ++divisor):
            return True
        # the number is not divisible by something under 20
        return False
    return True
