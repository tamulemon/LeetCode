'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

# quick but implementation of del doesn't garantee there is no additional array object created
def moveZeroes1(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)


# native method
# runs too slow for the standard???
def moveZeroes(nums):
    l = len(nums)
    n = 0
    while n < l:
        i = 0
        for i in range(l):   # note: need to make sure after a loop, i always starts from index 0
            if nums[i] == 0:
                lastInd = i
                for j in range(lastInd + 1, l):
                    nums[j - 1]= nums[j]
                nums[l- 1] = 0
                break
        n += 1



## only iterate the array once and swap in place
# also involve in moving zero only if needed

# trick: can have more than 1 pointer while only interate array once
# i will increment with the for loop regardless. zeroIndex will only move when number is not 0

def moveZeroes3(nums):
    zeroIndex = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zeroIndex] = nums[zeroIndex], nums[i] # if zeroIndex doesn't point to a number that is 0, it'll keep moving with i and swap with itself, so basically no change
            zeroIndex += 1 # zeroIndex only increment when not point to 0, will not move once point to 0


nums = [0, 0, 1]
nums2 = [0, 0, 1,3, 0 , 9]

# moveZeroes(nums)
# moveZeroes(nums2)

moveZeroes3(nums2)

print nums2
# print nums2

