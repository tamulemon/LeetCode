'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
import collections
def longestPalindrom(s):
    ct = collections.Counter(s)
    maxLen = 0
    hasOdd = False
    hasOne = False
    for k, v in ct.items():
        if v > 1:
            if v % 2 == 0:
                maxLen += v
            else:
                hasOdd = True
                maxLen += v - 1
        if v == 1:
            hasOne = True
    if hasOdd: # case s1, s2
        return maxLen + 1
    elif not hasOdd and hasOne: # case s3
        return maxLen + 1
    else:
        return maxLen

s1 = 'bananas'
s2 = 'ccc'
s3 = 'abccccdd'

print longestPalindrom(s1)
print longestPalindrom(s2)
print longestPalindrom(s3)
