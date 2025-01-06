'''
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
Return the final string after all such shifts to s are applied.

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)
        for left, right, d in shifts:
            prefix[right+1]+=1 if d else -1
            prefix[left]+=-1 if d else 1
        
        diff = 0
        res = [ord(c)-ord("a") for c in s]
        
        for i in reversed(range(len(prefix))):
            diff+=prefix[i]
            res[i-1]=(diff + res[i-1])%26

        s = [chr(ord("a")+n) for n in res]
        return "".join(s)
'''
Approach:
1. Approach uses prefix sum. For example if the shift is [1,2] and d is 1 then we 'add' from 0,2 and then subtract 1 for 0-1
2. Find the diff between the chracters and put in res-> gives ascii value
3. Iterating from the back of prefix, add difference for each prefix[i] and add diff to res[i-1]%26
4. Convert back to character for every character in the list res
'''
