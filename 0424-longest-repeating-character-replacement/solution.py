class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxlen = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxlen = max(maxlen, count[s[r]])
            if (r - l + 1) - maxlen > k:
                count[s[l]] -= 1
                l += 1
        return(r - l + 1)
