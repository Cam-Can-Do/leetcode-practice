class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""

        countsT = {}
        for letter in t:
            countsT[letter] = countsT.get(letter, 0) + 1

        have = 0
        need = len(countsT)
        
        res = [-1, -1]
        reslen = float("infinity")

        l = 0
        window = {}
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in countsT and window[char] == countsT[char]:
                have += 1

            while have == need:
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countsT and window[s[l]] < countsT[s[l]]:
                    have -= 1
                l += 1
        if reslen == float("infinity"):
            return ""
        else:
            return s[res[0]:res[1] + 1]




