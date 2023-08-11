class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = {}
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            # have a repeating character, need to shrink window
            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

                
                

        
