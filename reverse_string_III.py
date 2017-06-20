'''
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

def reverseString(inputStr):
    return inputStr[::-1]

def reverseStr3(inputStr):
    prevSpace = 0
    outputStr = ""
    for i in range(len(inputStr)):
        if inputStr[i] == ' ':
            outputStr += reverseString(inputStr[prevSpace:i]) + ' '
            prevSpace = i + 1
    outputStr += reverseString(inputStr[prevSpace:])
    return outputStr

str = "Let's take LeetCode contest"

print reverseStr3(str)