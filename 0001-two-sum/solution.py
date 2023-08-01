class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contained = {}
        for i, val in enumerate(nums):
            if target - val in contained:
                return [i, contained[target - val]]
            contained[val] = i
        
