class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contents = {}

        for index, value in enumerate(nums):
            if (target - value) in contents:
                return [index, contents[target-value]]
            else:
                contents[value] = index
