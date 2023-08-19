class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        highestCount = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            highestCount = max(counts[s[r]], highestCount)

            if r - l + 1 - highestCount > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1
            
        return r - l + 1


        
