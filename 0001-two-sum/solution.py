class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contained = {}
        for i, num in enumerate(nums):
            if target - num in contained:
                return [i, contained[target - num]]
            else: 
                contained[num] = i
            
