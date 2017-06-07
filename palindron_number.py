# whether a number is palindrome, without extra spaceclass
import math

# This doesn't work if there is 0 in the middle of the numebr
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or x == 10:
        return False
    while x > 10:
        length = int(math.floor(math.log10(x)))
        head = x  // math.pow(10, length)
        tail = x % 10
        if head != tail:
            return False
        else:
            x = (x - tail - head * math.pow(10, length))/10
    return True





def is_Palindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    if x // 10 == 0:
        return True
    length = int(math.floor(math.log10(x)))
    half_len = int(round(length/float(2)))
    for i in range(half_len):
        head = x  // math.pow(10, length - i) % 10
        tail = x % math.pow(10, i + 1) // math.pow(10, i)
        if head != tail:
            return False
    return True

print is_Palindrome(10)