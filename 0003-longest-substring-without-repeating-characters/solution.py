class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxlen = 0
        templen = 0
        substr = set()

        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                templen -= 1
                l += 1
            substr.add(s[r])
            templen += 1
            maxlen = max(templen, maxlen) 
        return maxlen
