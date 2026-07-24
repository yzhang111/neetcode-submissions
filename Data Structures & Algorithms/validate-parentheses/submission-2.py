class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            '(':')',
            '{':'}',
            '[':']'
        }

        for char in s:
            if char in pair:
                stack.append(char)
            elif char in pair.values():
                if stack:
                    open_bracket = stack.pop()
                    if not pair[open_bracket] == char:
                            return False
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        else: 
            return False