class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_amt = 0

        while l <= r:
            max_amt = max(max_amt, (r - l) * min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_amt
            


        
