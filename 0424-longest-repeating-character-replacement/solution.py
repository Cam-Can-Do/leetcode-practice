class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        maxlen = 0

        window = {}
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            maxlen = max(maxlen, window[s[r]])

            while r - l + 1 - maxlen > k:
                window[s[l]] -= 1
                l += 1
        return r - l + 1
            
        
