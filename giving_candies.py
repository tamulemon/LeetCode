'''
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 

Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].

'''

def distributeCandies(candies):
    uniqueCandies = set(candies)
    return min(len(uniqueCandies), len(candies)/2)