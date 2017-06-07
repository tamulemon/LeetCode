# import math
def merge_sort(input_arr):
    if len(input_arr) == 1:
        return input_arr
    half = len(input_arr) // 2
    left =  merge_sort(input_arr[ : half])
    right =  merge_sort(input_arr[half : ])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            # right.pop(j)
            j += 1
    if i == len(left) and j < len(right):
        merged.extend(right[j:])
    if j == len(right) and i < len(left):
        merged.extend(left[i:])
    return merged


if __name__ == '__main__':
	print merge_sort([3, -4, 2.3, 4, 5, 94, 0, 0, 9, 4, 5])