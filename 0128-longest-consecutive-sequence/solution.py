class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 in numSet:
                # not the start of a sequence
                continue
            cur = num + 1
            tempLen = 1
            while (cur) in numSet:
                cur += 1
            tempLen = cur - num
            res = max(tempLen, res)
        return res
