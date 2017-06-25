# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# brute force
def sum_2_number(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# dict
def sum_2_number2(nums, target):
    pos_dict = {}
    for i in range(len(nums)):
        if nums[i] not in pos_dict.keys():
            pos_dict[nums[i]] = [i]
        else:
            pos_dict[nums[i]].append(i)
        comple = target - nums[i]
        if comple in pos_dict.keys() and i != pos_dict[comple][0]:
            if comple != nums[i]:
                return [pos_dict[nums[i]][0], pos_dict[comple][0]]
            else:
                return pos_dict[nums[i]]


# fast
def sum_2_number2(nums, target):
    pos_dict = {}
    for i in range(len(nums)):
        if nums[i] in pos_dict.keys():
            return [pos_dict[nums[i]], i]
        else:
            pos_dict[target-nums[i]]= i


int_arr = [3, 2, 4]
target = 6

print sum_2_number2(int_arr, target)


## derived sum_3
# list[0], sum_2(list[1:]) -- still n2


################################
# if the array is sorted, no duplicated number, and only 1 pair will return target number

# this is similar to merge sort mechanism, using a low and a high pointer
def sum2sorted(list, target):
    i = 0
    j = len(list) - 1
    while i < j:
        if list[i] + list[j] > target:
            j -= 1
        elif list[i] + list[j] < target:
            i += 1
        else:
            return [i, j]
    return []

list = [2, 5, 7, 11]
target = 9
print '----------------'
print sum2sorted(list, target)