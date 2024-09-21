class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contained = {} # maps value to index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in contained:
                return [contained[diff], i]
            contained[n] = i
        
