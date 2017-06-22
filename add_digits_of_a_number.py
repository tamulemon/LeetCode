'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

'''

#recursive
import math
def addDigits(num):
    while num >= 10:
        sum = 0
        while num > 0:
            sum += num % 10
            num = num //10
        num = sum
    return num

num = 38

print addDigits(num)
