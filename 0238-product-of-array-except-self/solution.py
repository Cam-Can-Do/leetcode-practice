class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        preval = 1
        for i in range(len(nums)):
            if i > 0:
                preval *= nums[i - 1]
            prefixes.append(preval)

        postfixes = []
        postval = 1
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                postval *= nums[i + 1]
            postfixes.insert(0, postval)

        res = []
        for i in range(len(nums)):
            res.append(prefixes[i] * postfixes[i])
        return res

        
