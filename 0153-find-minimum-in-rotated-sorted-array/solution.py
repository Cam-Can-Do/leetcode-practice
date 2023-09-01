class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])

            # section is rotated
            if nums[m] > nums[r]:
                    l = m + 1
            # section is not rotated -- normal binary search
            else:
                    r = m - 1
        return res

        
