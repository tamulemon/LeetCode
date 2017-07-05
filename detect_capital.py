'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False

'''

# capital = set()
# for i in range(ord('a'), ord('z')):
#     capital.add(chr(i))
# print capital
#
# lower = set(map(lambda x: x.lower(), capital))
#
# print lower

def detectCapitalUse(word):
    capital = set()
    lower = set()

    for i in range(ord('A'), ord('Z') + 1):
        capital.add(chr(i))

    lower = set(map(lambda x: x.lower(), capital))

    if set(word) <= capital or set(word) <= lower or (set(word[1:]) <= lower and set(word[0]) <= capital):
        return True
    else:
        return False

# word1 = "ABC"
# word2 = 'Hppy'
# word3 = 'birthday'
# word4 = 'whatHappened'
word5 = 'Z'

# print detectCapitalUse(word1)
# print detectCapitalUse(word2)
# print detectCapitalUse(word3)
# print detectCapitalUse(word4)
print detectCapitalUse(word5)
