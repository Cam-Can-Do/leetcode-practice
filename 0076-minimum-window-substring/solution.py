class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need to count the frequencies of letters in t
        tCounts = {}
        for letter in t:
            tCounts[letter] = tCounts.get(letter, 0) + 1
        
        have = 0
        need = len(tCounts)

        res = [-1, -1]
        reslen = float("inf")

        window = {}
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tCounts and window[s[r]] == tCounts[s[r]]:
                have += 1
            
            while have >= need:
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in tCounts and window[s[l]] < tCounts[s[l]]:
                    have -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        if reslen != float("inf"):
            return s[res[0]:res[1]+1]
        else:
            return ""



        
        
