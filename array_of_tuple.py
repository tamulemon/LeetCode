#  interesting default sort on the first element of tuple
arr = [(4, 5), (2, 4), (1, 3), (8, 9)]
arr.sort()
print arr


# list.sort() method is only defined for lists. In contrast, the sorted() function accepts any iterable.
arr = [(4, 5), (2, 4), (1, 3), (8, 9)]
arr  = sorted(arr, key = lambda tup : tup[0])
print arr

#manually do it
# take the first element, create an array, sort
# loop through the new array and the original array, if tup[0] = arr[i], append to output array
# return output array

#manually do it
# take the first element, create an array, sort
# create a dict: {tup[0] : tup}
# compare the dict and the new array,synthesize a new array



# assign new value to a tupple

tup = (2, 5)
int = 4
if int < tup[1]:
    tup = (tup[0], int) # this works because the entire tupple gets reaasigned
    # tup[1] = int # doesn't work because tupple is unmutable
print tup
