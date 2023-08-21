class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)

            if s1 != s2:
                s1 = abs(s1)
                s2 = abs(s2)
                remaining = max(s1, s2) - min(s1, s2)
                heapq.heappush(maxHeap, -remaining)
        if not maxHeap:
            return 0
        return -maxHeap[0]
                
        
