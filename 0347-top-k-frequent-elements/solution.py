class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freqs = [[] for i in range(len(nums) + 1)]
        for num, freq in counts.items():
            freqs[freq].append(num)

        res = []
        
        for i in range(len(freqs) - 1, -1, -1):
            for num in freqs[i]:
                if k == 0:
                    return res
                else:
                    res.append(num)
                    k -= 1
        return res

        
