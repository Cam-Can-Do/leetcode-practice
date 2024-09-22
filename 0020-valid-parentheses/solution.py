class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')':'(', '}':'{', ']':'['}
        
        ordering = []

        for char in s:
            if char not in close_to_open:
                ordering.append(char)
                continue
            if not ordering or ordering[-1] != close_to_open[char]:
                return False
            ordering.pop()
        return not ordering
