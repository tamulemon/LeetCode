'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


import collections
import operator

s = "acadbfc"

s = map(lambda x : ord(x), s)
print s

print 97^98
# same as above, bitwise comparison
print operator.xor(97, 98)

s = "acadbfc"
print collections.Counter(s)

def firstUniqChar(s):
    return 0

# print firstUniqChar(s)