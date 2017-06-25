'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

    BA
    BB
    ...

    ZZ
    AAA
    AAB
    ....

    ABA
    ABB
    ...
'''

# some test
# print ord('A')
# print chr(65)
#
# dict = {}
# for i in range(65, 65 + 26):
#     dict[chr(i)] = i - 64
# print dict

# it's 26 based, so AB = 1 x 26  + 2 = 28
# BA = 2x26 + 1
# ZZ = 26 x 26 + 26
# AAA = 1x 26x26x26 + 1x26 + 1

import math
def titleToNumber(s):
    dict = {}
    for i in range(65, 65 + 26):
        dict[chr(i)] = i - 64

    l = len(s)
    num = 0
    for j in range(l):
        digit = dict[s[j]]
        num += digit * int(math.pow(26, l - j - 1))
    return num

s = "AB"

print titleToNumber(s)