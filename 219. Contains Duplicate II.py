'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        number = {}

        for i,num in enumerate(nums): #enumerate makes it (0,num),(1,num2)
            if num in number and i-number[num]<=k: #checks if num is in map, check if the existing i and current i have a diff of k
                return True
            
            number[num] = i #add num in dictionary
        return False
