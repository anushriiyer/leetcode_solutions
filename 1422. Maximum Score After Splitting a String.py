'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
'''
#Simpler method
class Solution:
    def maxScore(self, s: str) -> int:
        right_score=0
        max_score=0
        for i in range(len(s)):
            if s[i]=='1':
                right_score+=1
        left_score=0
        for i in range(len(s)-1):
            if s[i]=='0':
                left_score+=1
            else:
                right_score-=1
            max_score=max(max_score,right_score+left_score)
        return max_score

#Longer prefix sum
class Solution:
    def maxScore(self, s: str) -> int:
        left = [0]*len(s)
        right = [0]*len(s)
        result = [0]*len(s)   

        for i in range(len(s)):
            if i ==0:
                count = 0
            else:
                count = left[i-1]

            if s[i]=="0":
                count+=1
            left[i]= count
        
        for i in range(len(s)-1,-1,-1):
            if i == len(s)-1:
                count2 = 0
            else:
                count2 = right[i+1]
            if s[i] == "1":
                count2+=1
            right[i]=count2

        max_score = 0
        for i in range(len(left)-1):
            score = left[i]+right[i+1]
            max_score = max(max_score,score)
        return max_score


        
