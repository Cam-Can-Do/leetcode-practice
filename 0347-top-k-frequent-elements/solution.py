class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        quantities = [[] for i in range(len(nums) + 1)]

        for integer, quantity in counts.items():
            quantities[quantity].append(integer)
        
        amt_added = 0
        res = []
        for i in range(len(quantities) - 1, 0, -1):
            for entry in quantities[i]:
                res.append(entry)
                amt_added += 1
                if amt_added == k:
                    return res

