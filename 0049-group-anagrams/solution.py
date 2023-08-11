class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            my_sorted = "".join(sorted(word))
            if my_sorted not in groups:
                groups[my_sorted] = []
            groups[my_sorted].append(word)
        res = []
        for _, group in groups.items():
            res.append(group)
        return res

        
