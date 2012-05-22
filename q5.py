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

# Another way:
##! /usr/bin/env python
#
#def look_for_it(start):
#    # keep going until we find it
#    while (True):
#        ran = 1
#        for divisor in range(2,21):
#            # try next start
#            if start % divisor != 0:
#                break
#            else:
#                ran = ran + 1
#        # if loop ran 20 times then we have a winner
#        if ran == 20:
#            return start
#        start = start + 1
#
#if __name__=="__main__":
#    start = 380
#    print look_for_it(start)
