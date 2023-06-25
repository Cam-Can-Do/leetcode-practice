class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while True:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l+1, r+1]
            elif val < target:
                l += 1
            elif val > target:
                r -= 1



