'''Products of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
#Approach 1 (Division)
lass Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        for num in nums:
            if num == 0:
                zero_count +=1
                continue
            product*=num
            if zero_count>1:
                break
        
        if zero_count>1:
            nums = [0]*len(nums)
        
        elif zero_count ==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i] = product
                else: nums[i] = 0
        
        else:
            for i in range(len(nums)):
                nums[i] = product//nums[i]
        return nums       

#Approach 2 (Prefix and Suffix)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        result = [0]*len(nums)
        for i in range(len(nums)):
            product = 1
            j = i
            while j!=0:
                product*=nums[j]
                j-=1
            product *=nums[0]
            prefix[i]=product
        
        for i in range(len(nums)-1,-1,-1):
            product = 1
            j = i
            while j!=len(nums)-1:
                product*=nums[j]
                j+=1
            product *=nums[len(nums)-1]
            suffix[i]=product


        for i in range(len(nums)):
            preval = prefix[i-1] if i>0 else 1
            sufval = suffix[i+1] if i+1<len(nums) else 1
            result[i]=preval*sufval
        return result

#Simpler Version
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suffix
            suffix*=nums[i]
        
        return result

            
'''
Code Explanation:
1. Define prefix, suffix and result lists
2. Add in prefixes aka products from the beginning to the current number at prefix[current]
3. Add in suffixes aka products from the end to the current number at suffix[current]
4. The result comes out to be prefix[i-1]*suffix[i+1] (One needs to be very careful of boundary conditions)

'''
