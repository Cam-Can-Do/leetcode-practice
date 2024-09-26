class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm = ''
        for char in s:
            if char.isalnum():
                norm += char.lower()
        return norm == norm[::-1]

