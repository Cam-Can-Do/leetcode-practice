class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        discovered = set()
        for element in nums: 
            if element in discovered:
                return True
            discovered.add(element)
        return False

