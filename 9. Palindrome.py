'''Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        reverse = str(x) [::-1]

        if str(x) == reverse:
            return True

        return False

'''
Code Explanation:
1. If x is negative return False
2. Reverse the number as a string (flip through negative slicing)
3. Compare numbers, return True if same
'''
