class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for char in s:
            if char in pair:
                if len(stack) == 0:
                    return False
                if stack[-1] != pair[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0