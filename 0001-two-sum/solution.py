class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contained = set()

        for i, num in enumerate(nums):
            if target - num in contained:
                return [i, nums.index(target-num)]
            contained.add(num)
        return False
        
