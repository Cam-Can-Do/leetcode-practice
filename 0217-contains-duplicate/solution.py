class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contained = set() 
        for num in nums:
            if num in contained:
                return True
            else:
                contained.add(num)
        return False
        
