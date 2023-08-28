class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        while k > 0 and maxHeap:
            res = -(heapq.heappop(maxHeap))
            k -= 1
        return res
        
