# 224. Basic Calculator

class Solution:
    def calculate(self, s: str) -> int:
        ans, curr, sign, stack = 0, 0, 1, []
        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)
            elif char in '+-':
                ans += curr * sign
                sign = -1 if char == "-" else 1
                curr = 0
            elif char == "(":
                stack.append(ans)
                stack.append(sign)
                ans, sign = 0, 1
            elif char == ")":
                ans += curr * sign
                ans *= stack.pop()
                ans += stack.pop()
                curr = 0
        return ans + (curr * sign)

'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''