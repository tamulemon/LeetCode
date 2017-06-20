'''
Input: 
nums = 
[[1,2], [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]


Input: 
nums = 
[[1,2],[3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

'''
def matrixReshape(num, r, c):
    r1 = len(num)
    c1 = len(num[0])
    flatOut = []
    output = []

    if r1 * c1  != r * c:
        return num
    for i in range(r1):
        flatOut.extend(num[i])
    for j in range(0, len(flatOut) - c + 1, c):
        output.append(flatOut[j : j + c])
    return output

num = [[1, 2], [3, 4]]

print matrixReshape(num, 1, 4)
