'''You are given two arrays with positive integers arr1 and arr2.
A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.
A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have common prefixes 565 and 5655 while 1223 and 43456 do not have a common prefix.
You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.
Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

Example 1:
Input: arr1 = [1,10,100], arr2 = [1000]
Output: 3
Explanation: There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.'''

#Approach 1 (Leads to Run-Time Error)
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        longest = 0
        for i in range(len(arr1)):
            #define the smaller value of the two arrays as the prefix
            for j in range(len(arr2)):
                if arr1[i]<arr2[j]:
                    prefix = str(arr1[i])
                    compare = str(arr2[j])
                else:
                    prefix = str(arr2[j])
                    compare = str(arr1[i])

              #keep reducing prefix until a match is found
                while not compare.startswith(prefix):
                    prefix = prefix[:-1]
              #if prefix is empty, longest remains unchanged, otherwise, if the length of prefix is greater than longest, update
                if prefix != "" and len(prefix)>longest:
                    longest = len(prefix)

        return longest

#IMPORTANT: Approach 2 (Hash Set)
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixmap = {}
        
        for num in arr1:
            num = str(num)
            prefix = ""
            for ch in num:
                prefix+=ch
                prefixmap[prefix]=prefixmap.get(prefix,0)+1
        
        max_length = 0
        for num in arr2:
            num = str(num)
            prefix =""
            for ch in num:
                prefix+=ch
                if prefix in prefixmap:
                    max_length = max(max_length,len(prefix))
        return max_length        

'''
Code Explanation:
1. For each integer in Array 1, convert to string
2. for letter in string, add to prefix, get from prefix map if prefix exists, else assign 0 and add 1 to count
3. Iteratee similarly, check if prefix exists in prefix map and then update the max_length if current prefix length is bigger
'''
