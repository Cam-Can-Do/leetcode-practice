class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            solution[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            solution[i] *= postfix
            postfix *= nums[i]
        
        return solution
