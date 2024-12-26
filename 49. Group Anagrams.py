'''
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sort = tuple(sorted(word))
            if sort in hashmap:
                hashmap[sort].append(word)
            else:
                hashmap[sort] = [word]

        output = list(hashmap.values())
        return output
'''
Code Explanation:
1. Define a hashmap and make a sorted tuple of the word the key
2. Match words based on their sorted version, if they are in hashmap, then append to the existing list
3. Else add to hashmap
'''
