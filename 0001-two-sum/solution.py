class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in val_to_index:
                return [i, val_to_index[diff]]
            val_to_index[num] = i
