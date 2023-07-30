class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sletters = {}
        for letter in s:
            if letter in Sletters:
                Sletters[letter] += 1
            else:
                Sletters[letter] = 0
        Tletters = {}
        for letter in t:
            if letter in Tletters:
                Tletters[letter] += 1
            else:
                Tletters[letter] = 0
        return Tletters == Sletters

