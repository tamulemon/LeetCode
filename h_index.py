'''
given an int array, return a maxium x, that at least x number of member in the array is larger or equal than x
example : [1, 2, 0, 5, 8, 10]
x = 3 (3 number in the array is larger or equal than 3)
'''
def hIndex(inputList):
    # 0 <= x <= len(list)
    inputList.sort()
    x = 0 # min
    i = 0
    length = len(inputList)
    while x <= length and i < length:
        while inputList[i] < x and i < length:
            i += 1

        if length - i + 1 > x:
            x += 1
            if x == length:
                return x - 1
            if length - i + 1 == x:
                return x

def hIndex2(inputList):
    inputList.sort()
    n = len(inputList)
    for i in range(n):
        if inputList[i] >= n - i:
            return n - i
    return 0


l1 = [3, 4, 2, 2, 6, 7, 0, 12] #4
l2 = [0, 1, 2, 5, 8, 10] #3
l3 = [6, 6, 6] #3
l4 = [2, 2, 2] #2
l5 = [0, 0, 0] #0
l6 = [3] #1


# the only circumstance will return 0, is all member in array is 0
# the onlyl circumstance will return len, is max(list) >= len
