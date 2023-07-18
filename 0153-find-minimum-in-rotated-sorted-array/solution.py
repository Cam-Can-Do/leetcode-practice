class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1

        # want to find the minimum element...
        # so binary search except we need to determine which half we're in..
        
        # examples:
        # 4 5 6 7 1 2 3
        # 7 1 2 3 4 5 6

        while l <= r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1
            res = min(res, nums[m])
        return res

