#! /usr/bin/env python

def sum_of_squares():
    sum = 0
    for num in range(1, 101):
        sum = sum + num*num
    return sum

def square_of_sum():
    sum = 0
    for num in range(1, 101):
        sum = sum + num
    return sum*sum

if __name__=="__main__":
    print square_of_sum() - sum_of_squares()
