def quick_sort(nums, i, j):
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

    if i < j:
        pivot = sort_pivot(nums, i, j)
        left_i = i
        left_j = pivot - 1
        right_i = pivot + 1
        right_j = j

        if left_i < left_j:
            quick_sort(nums, left_i, left_j)
        if right_i < right_j:
            quick_sort(nums, right_i, right_j)
    return nums


def sort_pivot(listToSort, i, j): # i is the starting point, j is the end point
    pivot = listToSort[i] # start with the first element as pivot value
    left = i + 1 # move left to the next position
    right = j
    while left <= right: # left can not exceed right
        if listToSort[left] <= pivot:
            left += 1
        if listToSort[right] >= pivot:
            right -= 1
        if right < left: # break immediately when left exceeds right
            break
        if listToSort[left] >  listToSort[right]: # swap left and right value if left value> right value
            temp = listToSort[right]
            listToSort[right] = listToSort[left]
            listToSort[left] = temp

    temp = listToSort[right]        # swap pivot and right boarder, right boarder becomes the permanent pivot pivot
    listToSort[right] = listToSort[i]
    listToSort[i] = temp
    return right            # return pivot positino


if __name__ == '__main__':
    nums = [6, 5, 12, -0.5, 6.8, -19, -5, 0, -5, 2, 3, 6]
    print quick_sort(nums, 0, len(nums)-1)