

import math

def largest_common_factor(num1, num2):
    # find all factors of num1
    # test whether any of them is a factor of num2
    # replace by max
    common_factor = float("-inf")
    if num2 % num1 == 0: #still O(n) but a shorter linear
        return num1
    if num1 % num2 ==0:
        return num2
    for i in range(2, int(math.sqrt(num1)) + 1):
        if num1 % i == 0 and num2 % i == 0:
            if i > common_factor:
                common_factor = i
    return common_factor

print largest_common_factor(90, 995)


#######################################################
def is_prime(num):
    if num == 0:
        return False
    if num in [1, 2]:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2): # incremental 2 in the loop, only need to check to the square root
        if num % i == 0 :
            return False
    return True

print is_prime(49)

#################################################

def all_prime_num_less_than(x):
    return True


