# Example1: x = 123, return 321
# Example2: x = -123, return -321

import math

def reverse_int(input_int):
    if input_int == 0:
        return 0
    if input_int > math.pow(2, 31) - 1 or input_int < -1 * math.pow(2, 31):
        return 0
    sign = input_int/math.fabs(input_int)
    input_int = math.fabs(input_int)
    total_len =  int(math.floor(math.log10(input_int)))
    output_int = 0
    leftover = input_int
    for i in range(total_len):
        digit = leftover % 10
        leftover = leftover // 10
        output_int += math.pow(10, total_len - i) * digit
    output_int = int((output_int + leftover)*sign)
    if output_int > math.pow(2, 31) - 1 or output_int < -1 * math.pow(2, 31):
        return 0
    else:
        return output_int

input_int =98761
#
# print reverse_int(input_int)

x1 = 1534236469
x2 = math.pow(2, 31) - 1
if x1 > x2:
    print 'yes'
else:
    print 'no'
