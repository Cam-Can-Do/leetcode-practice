class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float("inf")

        while l <= r:
            m = (r + l) // 2
            res = min(res, nums[m])
            
            if nums[m] > nums[r]:   # window is rotated
                l = m + 1

            else:   # window in ascending order
                r = m - 1
            
        return res
