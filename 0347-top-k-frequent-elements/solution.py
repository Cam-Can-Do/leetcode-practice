class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        # next, need to group/sort numbers by frequency

        groups = [[] for i in range(len(nums) + 1)]

        for num, freq in freqs.items():
            groups[freq].append(num)

        res = []

        for i in range(len(groups) - 1, -1, -1):
            # i is index in groups... groups[i] is an array
            vals = groups[i]
            for val in vals:
                if k == 0:
                    return res
                res.append(val)
                k -= 1
        return res
