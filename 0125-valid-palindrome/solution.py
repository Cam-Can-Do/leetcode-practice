class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i <= ((len(s) - 1) / 2):
            if s[i] != s[j]:
                return False
            i += 1
            j -=1
        return True

