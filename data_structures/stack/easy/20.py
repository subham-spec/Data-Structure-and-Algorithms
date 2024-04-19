# 20. Valid Parenthesis
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        opening = ['(','{','[']
        for ch in s:
            print(ch)
            if ch in opening:
                stk.append(ch)
            else:
                if not stk:
                    return False
                char = stk.pop()
                if not ((ch == ')' and char == '(') or
                        (ch == '}' and char == '{') or
                        (ch == ']' and char == '[')):
                    return False

        if not stk:
            return True
        return False