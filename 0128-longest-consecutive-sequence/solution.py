class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            # the start of a sequence
            curlen = 0
            if num - 1 not in numSet:
                cur = num
                while cur in numSet:
                    curlen += 1
                    longest = max(curlen, longest)
                    cur += 1
        return longest
                




        
