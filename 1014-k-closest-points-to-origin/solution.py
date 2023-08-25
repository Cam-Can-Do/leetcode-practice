class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            maxHeap.append([(abs(point[0]) ** 2) + abs(point[1]) ** 2, point[0], point[1]])

        res = []

        heapq.heapify(maxHeap)
        while len(res) < k:
            res.append(heapq.heappop(maxHeap)[1:])
        return res
        
