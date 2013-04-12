#!/usr/bin/python
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""
# offset alphabet.find(X)
alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    sum_of_names = 0
    names = sorted(map(lambda x:x.split('"')[1], open('names.txt').read().split(',')))
    for pos,name in enumerate(names):
        sum_of_letters = 0
        for letter in name:
            sum_of_letters += alphabet.find(letter)
        sum_of_names += sum_of_letters*(pos+1)
    print sum_of_names


if __name__=='__main__':
    main()
