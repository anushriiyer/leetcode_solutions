'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l<r:
                threesum = nums[i] + nums[l]+nums[r]
                if threesum >0:
                    r-=1
                elif threesum <0:
                    l+=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return result

  '''
  Approach:
  1. Iterate through all a (first number), if the number is the same as previous number then continue (sorted array)
  2. 2 pointer in rest of the numbers
  3. If it adds to 0, add to result, increase l (r will decrease if required), if l is the same as previous number then add to l
  '''
