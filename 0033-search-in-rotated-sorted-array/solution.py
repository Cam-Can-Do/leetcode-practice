class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            # section is sorted
            if nums[m] <= nums[r]:
                # if target is in the left half
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                # target is in the right half
                else:
                    r = m - 1
            # section is rotated
            else:
                # target is in left half
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                # target is in right half
                else:
                    l = m + 1

        return -1
        
