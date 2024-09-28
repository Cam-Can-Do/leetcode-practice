class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contained = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in contained:
                return [i, contained[diff]]
            contained[num] = i
        
