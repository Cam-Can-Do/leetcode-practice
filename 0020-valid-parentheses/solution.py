class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char not in close_to_open:
                stack.append(char)
                continue
            if not stack or close_to_open[char] != stack[-1]:
                return False
            stack.pop()
        return not stack
