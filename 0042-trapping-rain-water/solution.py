class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        waterTrapped = 0
        
        while l <= r:
            if height[l] < height[r]:
                leftMax = max(height[l], leftMax)
                waterTrapped += leftMax - height[l]
                l += 1
            else:
                rightMax = max(height[r], rightMax)
                waterTrapped += rightMax - height[r] 
                r -= 1
        return waterTrapped
            
