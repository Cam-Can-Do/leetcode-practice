class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        while l <= r:
            pointer = int((r - l) / 2) + l
            if nums[pointer] == target:
                return pointer
            elif nums[pointer] < target:
                l = pointer + 1
            elif nums[pointer] > target:
                r = pointer - 1
        return -1 
