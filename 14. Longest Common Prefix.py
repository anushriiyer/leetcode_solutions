'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if len(prefix)==0:
                    return ""
        
        return prefix

'''
Code Explanation:
1. Set the first word of the list to the prefix
2. Iterate through the other words in the list and check if they start with the prefix
3. While the condition is not met, trim the prefix by one from the end
4. If prefix becomes empty then return empty string
'''
