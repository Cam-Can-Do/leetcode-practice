class Solution:
    def isValid(self, s: str) -> bool:
        closings = {')':'(', ']':'[','}':'{'}
        stack = []

        for char in s:
            if char in closings and stack:
                if stack[-1] != closings[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        else:
            return True

