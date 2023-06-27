class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for index, value in enumerate(nums):
            if target - value in numsDict:
                return [index, numsDict[target - value]]
            numsDict[value] = index
