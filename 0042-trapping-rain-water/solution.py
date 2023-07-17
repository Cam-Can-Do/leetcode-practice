class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        sum = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                sum += leftMax - height[l]
            elif height[l] > height[r]:
                r -= 1
                rightMax = max(rightMax, height[r])
                sum += rightMax - height[r]

        return sum
        
