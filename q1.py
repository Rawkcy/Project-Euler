#! /usr/bin/env python

# find sum of all multiples of 3 or 5 below 1000

# run for loop from 0 to 1000
# check if it's a multiple of 3 or 5
# if yes then plus equal to sum
# if no then continue

sum1 = 0
for i in range(1, 1000):
    if i%3==0 or i%5==0:
        sum1 += i
print sum1
