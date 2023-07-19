class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}

        for letter in s1:
            counts1[letter] = counts1.get(letter, 0) + 1
        
        counts2 = {}
        
        l = 0
        for r in range(len(s2)):
            counts2[s2[r]] = counts2.get(s2[r], 0) + 1
            if counts1 == counts2:
                return True

            if (r - l + 1) >= len(s1):
                counts2[s2[l]] -= 1
                if counts2[s2[l]] == 0:
                    del counts2[s2[l]]
                l += 1

        return False



