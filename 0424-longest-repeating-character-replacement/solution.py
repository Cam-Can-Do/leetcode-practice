class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        maxlen = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxlen = max(maxlen, counts[s[r]])
            if r - l + 1 - maxlen > k:
                counts[s[l]] -= 1
                l += 1
        return (r - l + 1)


