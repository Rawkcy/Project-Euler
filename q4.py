#! /usr/bin/env python

class q4(self):
    def loop_divisible(self, num):
        # check if the number is divisible by 1 to 20
        divisor = 1
        while divisor <= 20:
            if num%divisor == 0:
                divisor += 1
            else:
                return False
        return True

    def find_lowest_divident(self, number):
        print self.loop_divisible(number)
        while(not self.loop_divisible(number)):
            test_number += 2
        return test_number

def recursion_divisible(num, divisor):
    # check if the number is divisible by 1 to 20
    if divisor <= 20:
        # if divisible
        if num%divisor == 0 and divisible(num, ++divisor):
            return True
        # the number is not divisible by something under 20
        return False
    return True
