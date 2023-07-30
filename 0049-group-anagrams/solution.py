class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedToAnagrams = {}

        for word in strs:
            sStr = "".join(sorted(word))
            if sStr not in sortedToAnagrams:
                sortedToAnagrams[sStr] = [word]
            else: 
                sortedToAnagrams[sStr].append(word)

        res = []
        for _, words in sortedToAnagrams.items():
            templist = []
            for word in words:
                templist.append(word)
            res.append(templist)
        return res

