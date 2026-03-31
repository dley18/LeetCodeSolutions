from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:


        heap = []

        results = []
        
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        for _ in range(k):
            smallest = heapq.heappop(heap)
            results.append([nums1[smallest[1]], nums2[smallest[2]]])
            if smallest[2] + 1 < len(nums2): 
                heapq.heappush(
                    heap, 
                    (nums1[smallest[1]] + nums2[smallest[2] + 1], smallest[1], smallest[2] + 1)
                )

        return results
            


            

        
