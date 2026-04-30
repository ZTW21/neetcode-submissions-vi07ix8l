class Solution:
    def isValid(self, s: str) -> bool:
        _map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for c in s:
            if c in _map:
                if stack and stack[-1] == _map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
