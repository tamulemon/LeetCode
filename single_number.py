'''
Given an array of integers, every element appears twice except for one. Find that single one.
'''
def singleNumber(nums):
    outputDict = {}
    for i in range(len(nums)):
        if nums[i] in outputDict.keys():
            outputDict.pop(nums[i], None)
        else:
            outputDict[nums[i]] = None
    return outputDict.keys()[0]


def singleNumber2(nums):
    return reduce(lambda x, y : x ^ y, nums)
arr = [1,2, 3,4, 5, 6, 7, 8]

print singleNumber2(arr)