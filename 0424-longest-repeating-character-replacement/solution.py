class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        counts = {}
        longest = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            longest = max(longest, counts[s[r]])

            if r - l + 1 - longest > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1
        return r - l + 1

        
