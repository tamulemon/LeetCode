inputList = ["apple", 'orange', 'banana', 'whatever']
import copy
# create all subsets
'''
C n 0
C n 1
...
C n n
 '''
# print inputList + ["happy"] --same as append

def subset(inputList):
    if len(inputList) == 0 :
        return [[]]

    additioalElement = inputList[0]
    restSubset = subset(inputList[1:])

    #this works and is short!!!!
    # return restSubset + [[additioalElement] + x for x in restSubset]

    # has to deep copy otherwise will mess up the stack
    newSubset = copy.deepcopy(restSubset)
    for x in restSubset:
        x .append (additioalElement)
    newSubset.extend((restSubset))
    return newSubset

    # return newSubset.extend((restSubset)) # this specificly doesn't work before append and Extend mutate the array and return 'None'
    # so for array concatenation, return [] + [] is better

print subset(inputList)