class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        for letter in s1:
            s1_counts[letter] = s1_counts.get(letter, 0) + 1
        
        l = 0
        window = {}

        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            if window == s1_counts:
                return True
            
            while r - l + 1 >= len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] <= 0:
                    del window[s2[l]]
                l += 1

        return False

        
