'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, 
each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. 
You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. 
Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: 
no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.



'''

# 1, 2, 3 can win
# 4 can not: 4 = 1 + 3, 2+ 2, 3+1
# 5 can: if do 1 + 4
# 6 can: if do 2 + 4
# so if a number - 1, -2, or -3 can result in a losing case, it can win

# so all 4's multiplication can not win

def canWinNim(n):
    if n <= 3:
        return True
    if n == 4:
        return False
    if n > 4:
        if canWinNim(n-1) and canWinNim(n - 2) and canWinNim(n - 3):
            return False
        else:
            return True

# so all 4's multiplication can not win
def canWinNim2(n):
    return (n % 4 != 0)

print canWinNim(12)


