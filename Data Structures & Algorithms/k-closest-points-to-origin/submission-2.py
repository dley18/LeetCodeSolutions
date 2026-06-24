class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, [distance, point[0], point[1]])

        for _ in range(k):
            point = heapq.heappop(heap)
            res.append([point[1], point[2]])

        return res
