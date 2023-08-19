class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsS = {}
        for char in s:
            countsS[char] = countsS.get(char, 0) + 1
        countsT = {}
        for char in t:
            countsT[char] = countsT.get(char, 0) + 1
        return countsT == countsS
        
