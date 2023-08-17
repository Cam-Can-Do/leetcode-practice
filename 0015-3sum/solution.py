class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        for i, a, in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if a > 0:
                break
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        return res

        
