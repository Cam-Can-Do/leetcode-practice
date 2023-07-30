class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r  = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
               return m
            elif nums[m] < nums[l]: # in rotated section
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: # not rotated, so do normal binary search
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
            
