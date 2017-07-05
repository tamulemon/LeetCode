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

# or
def firstUniqChar(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    index = [s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1
# print firstUniqChar(s)