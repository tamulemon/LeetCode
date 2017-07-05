'''
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

'''

def findMaxConsecutiveOnes(nums):
    length = 0
    maxLengh = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            length += 1
        if (nums[i] == 0) or (i == len(nums) - 1):
            if length > maxLengh:
                maxLengh = length
            length = 0
    return maxLengh

print findMaxConsecutiveOnes([1, 1, 0, 0, 1, 1, 1])