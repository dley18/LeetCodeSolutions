from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            root = heapq.heappop_max(stones)
            child = heapq.heappop_max(stones)

            if root == child:
                continue
            else:
                num = root - child
                heapq.heappush_max(stones, num)
            

        return heapq.heappop_max(stones) if len(stones) > 0 else 0            




solution = Solution()

num = solution.lastStoneWeight([4,3,4,3,2])

print(num)
