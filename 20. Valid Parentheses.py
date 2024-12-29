'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        pdict = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in pdict:
                if stack:
                    if stack.pop() == pdict[c]:
                        continue
                    else:
                        return False
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False


        
