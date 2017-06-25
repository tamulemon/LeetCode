'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

'''

# method1:
# can not do list(set(t) - set(s))[0], as if the added letter is already in s, it won't be caught

# method 2:
import collections
s = "abcd"
t = 'aabcd'
ct1 = collections.Counter(s) # counter object looks like dictionary
ct2 = collections.Counter(t)
print ct2 - ct1
print list(ct2-ct1)[0] # counter's key can be transformed into an array

# method 3:
j = map(ord, s + t) # change to ASCII number, to a list
print j

import operator
additional =  reduce(lambda x, y: operator.xor(x, y), j) #bitwise comparison
print chr(additional)

