class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        contained = set()
        maxlen = 0

        for r in range(len(s)):
            while s[r] in contained:
                contained.remove(s[l])
                l += 1
            contained.add(s[r])
            maxlen = max(len(contained), maxlen)
        return maxlen
