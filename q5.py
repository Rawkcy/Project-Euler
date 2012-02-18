#! /usr/bin/env python
class q5(object):
    def __init__(self, answer):
        self.answer = answer

    def loop_divisible(self, num):
        divisor = 2
        # check if the number is divisible by 1 to 20
        while divisor <= 20:
            if num%divisor == 0:
                divisor += 1
            else:
                return False
        return True

    def find_lowest_divident(self, answer):
        # keep looping until we find one that's true
        while(not self.loop_divisible(answer)):
            answer += 2
        return answer

if __name__=="__main__":
    answer = 20
    q5_run = q5(answer)
    print q5_run.find_lowest_divident(answer)

# def recursion_divisible(num, divisor):
#     # check if the number is divisible by 1 to 20
#     if divisor <= 20:
#         # if divisible
#         if num%divisor == 0 and divisible(num, ++divisor):
#             return True
#         # the number is not divisible by something under 20
#         return False
#     return True
