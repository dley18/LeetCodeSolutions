import heapq
from typing import List

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        day = 0
        apples_eaten = 0
        heap = []

        while day < len(days) or heap:

            if day < len(apples) and apples[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))

            while heap and day >= heap[0][0] :
                heapq.heappop(heap)

            if heap:
                batch = heapq.heappop(heap)
                expiration, apple_count = batch
                apple_count -= 1
                apples_eaten += 1
                if apple_count > 0:
                    heapq.heappush(heap, (expiration, apple_count))

            day += 1

        return apples_eaten