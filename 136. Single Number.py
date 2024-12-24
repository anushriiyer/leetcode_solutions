'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
'''

#Apprach 1: Uses O(N) space complexity
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num]= count.get(num,0)+1
        return [k for k,v in count.items() if v==1][0] #return first element of list that is retrieved where v is 1
        
#Approach 2: Use bitwise operator
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result^=num
        return result

'''
same number XOR will give 0
0 XOR with number gives number
'''
