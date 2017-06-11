# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance. 0<=x, y < 2^31 so unsigned 32 bit int
import math
def hamming_distinct(x, y):
    def convert_to_binary(y):
        leftover = y
        bi_arr_y = ''
        while leftover > 0:
            digit = leftover % 2
            bi_arr_y += str(digit) #theoretically the binary string should be bi_arr_y = str(digit) + bi_arr_y
            leftover = leftover // 2
        return bi_arr_y
    if x < y :
        temp = x
        x = y
        y = temp # make sure x is larger than y
    str_x = convert_to_binary(x)
    str_y = convert_to_binary(y)
    len_y = len(str_y)
    len_x = len(str_x)
    len_diff = len_x - len_y
    hamming_dis = 0
    for i in range(len_y):
        if str_x[i] != str_y[i]:
           hamming_dis += 1
    for j in range(len_y, len_x):
        if str_x[j] == '1':
            hamming_dis += 1
    return hamming_dis




print hamming_distinct(4, 1)