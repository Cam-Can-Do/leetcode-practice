class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')':'(', '}':'{', ']':'['}
        stack = []  # push most recent character (non-closing paren) to stack.
        # when we encounter a closing paren check that the top of stack is the corresponding opening paren
        
        for c in s:
            if c not in close_to_open:
                stack.append(c)
                continue
            if not stack or stack[-1] != close_to_open[c]:
                return False
            stack.pop()
        return not stack
