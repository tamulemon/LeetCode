'''Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image '''
# row 1: q, w, e, r, t, y, u, i, o, p
# row 2: a, s, d, f, g, h, j, k, l
# row 3: z, x, c, v, b, n, m
def findWords(words):
    dict = {}
    for alphabet in ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']:
        dict[alphabet] = 1
    for alphabet in ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']:
        dict[alphabet] = 2
    for alphabet in ['z', 'x', 'c', 'v', 'b', 'n', 'm']:
        dict[alphabet] = 3

    output = []
    j = 0
    for j in range(len(words)):
        word = words[j]
        first = True
        row = 0
        i = 0
        while i < len(word):
            if first:
                row = dict.get(word[i].lower())
                first = False
                i += 1
            else:
                if row != dict.get(word[i].lower()):
                    break
                else:
                    i += 1
        if i == len(word):
            output.append(word)
    return output




def findWords2(words): #using set, faster
    row1 = set('qwertyuiop') #same as set(['e', 'i', 'o', 'q', 'p', 'r', 'u', 't', 'w', 'y'])
    row2 = set ('asdfghjkl')
    row3 = set('zxcvbnm')
    output = []
    for word in words:
        wordSet = set(word.lower())
        if wordSet <= row1 or wordSet <= row2 or wordSet <= row3: # if subset
            output.append(word)
    return output

words = ["abdfs","ccc","a","qwwewm"]

print findWords(words)
print findWords2(words)