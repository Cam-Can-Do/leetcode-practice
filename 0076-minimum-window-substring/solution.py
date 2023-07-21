class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countsT = {}
        for char in t:
            countsT[char] = countsT.get(char, 0) + 1
        
        res = [-1, -1]
        reslen = float("infinity")

        have = 0
        need = len(countsT)

        window = {}
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countsT and window[c] == countsT[c]:
                have += 1 

            while have == need:
                if r - l + 1 < reslen:
                    res = l, r
                    reslen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countsT and window[s[l]] < countsT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if reslen != float("infinity") else ""




        
