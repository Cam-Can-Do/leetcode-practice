class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minim = nums[0]

        while l <= r:
            m = (l + r) // 2
            minim = min(nums[m], minim)
            if nums[m] > nums[r]: 
                l = m + 1
            else:
                r = m - 1
        return minim
