class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            res = max(res, len(substr))
        return res
