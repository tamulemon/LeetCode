def quick_sort(nums):
    ''' 
    The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, 
    put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, 
    and put all greater elements (greater than x) after x. All this should be done in linear time.
    
    :param pivot: index of the pivot point
           nums: number array 
    :return: 
    '''
    if len(nums) <= 1:
        return nums

    #because nums[pivot] is already at permenant position, it doesn't need to be sorted again
    pivot = sort_pivot(nums)[0]
    nums = sort_pivot(nums)[1]

    left = nums[:pivot]
    right = nums[pivot:]

    # use the leftmost as pivot point
    left = quick_sort(left)
    right = quick_sort(right)

    output = left.append(nums[pivot])
    output.extend(right)

    return output

def sort_pivot(list):
    pivot = list[0]
    i = 1
    j = len(list) - 1
    while i < j:
        if list[i] < pivot:
            i += 1
        if list[j] > pivot:
            j -= 1
        if list[i] >  list[j]:
            temp = list[j]
            list[j] = list[i]
            list[i] = temp
            i += 1
            j -= 1
    temp = list[i]
    list[i] = list[0]
    list[0] = temp
    return [i, list]

if __name__ == '__main__':
    nums = [6, 5, 12, 3, 0, -5, 0, -5, 2, 3, 6]
    print quick_sort(nums)