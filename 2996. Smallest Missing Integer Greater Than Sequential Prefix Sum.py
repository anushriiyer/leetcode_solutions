'''
You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

Example 1:
Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
'''

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                sum+=nums[i]
            
            else: break
        
        while sum in nums:
            sum+=1
        
        return sum

'''
Code Explanation:
1. Initialise sum with the first number in nums (determines the beginning of prefix)
2. Iterate from the nums[1], if current integer-previous integet == 1 then add them (part of prefix), else break the loop (longest prefix found)
3. While the sum is in the loop, keep adding to sum until a value not in the list is found, return that value sum 
'''
