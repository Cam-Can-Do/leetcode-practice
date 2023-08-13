class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0

        l = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1

            res = max(res, counts[s[r]])

            if r - l + 1 - res > k:
                counts[s[l]] -= 1
                l += 1
            
        return r - l + 1

        
