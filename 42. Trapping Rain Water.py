'''
42. Trapping Rain Water
Solved
Hard

Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        res = 0
        imax, jmax = height[i],height[j]
        while i<j:
            if height[i]<height[j]:
                i+=1
                imax = max(imax,height[i])
                res += imax - height[i]
            else:
                j-=1
                jmax = max(jmax,height[j])
                res+=jmax - height[j]
        return res
               
