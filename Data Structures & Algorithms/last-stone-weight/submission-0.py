class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            v1 = heapq.heappop_max(stones)
            v2 = heapq.heappop_max(stones)

            if v1 == v2:
                continue
            elif v1 > v2:
                v1 = v1 - v2
                heapq.heappush_max(stones, v1)
            else:
                v2 = v2 - v1
                heapq.heappush_max(stones, v2)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0