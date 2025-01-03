'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        i = 0
        j = len(height)-1
        while i<j:
            new_vol = (j-i)*min(height[i],height[j])
            vol = max(vol,new_vol)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return vol
'''
Code Explanation:
If the smaller height is i then increase i, else decrease j
'''
