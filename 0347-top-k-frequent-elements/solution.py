class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freqs = [[] for i in range(len(nums)+1)]

        for number, freq in counts.items():
            freqs[freq].append(number)

        res = []
        for i in range(len(freqs) - 1, 0, -1):
            curr_array = freqs[i]
            for num in curr_array:
                res.append(num)
                if len(res) == k:
                    return res

        
