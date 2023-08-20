class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        i = 0
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return None


            subset.append(nums[i])
            dfs(i+1)
        
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
