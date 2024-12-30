'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        
        if len(tokens)==1:
            return int(tokens[0])

        for token in tokens:
            if token in "+-*/":
                second = stack.pop()
                first = stack.pop()
                
                if token == "+":
                    stack.append(first+second)
                elif token == "-":
                    stack.append(first-second)
                elif token == "/":
                    stack.append(int(float(first) / second))
                elif token =="*":
                    stack.append(first*second)
            else:
                stack.append(int(token))
        
        return stack.pop()
        
