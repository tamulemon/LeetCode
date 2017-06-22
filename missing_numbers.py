'''
Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

'''


def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # For each number i in nums,
    # we mark the number that i points as negative.
    # Then we filter the list, get all the indexes
    # who points to a positive number.
    # Since those indexes are not visited.


    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print findDisappearedNumbers(arr)
