class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # right section is not sorted, rotated
            if nums[m] > nums[r]:
                if nums[l] > target or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

            # right is in sorted order
            else:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1
