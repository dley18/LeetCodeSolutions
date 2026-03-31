from typing import List
import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        heapq.heapify_max(target)

        if target == [1]:
            return True

        total = sum(target)
        while True:            
            largest = heapq.heappop_max(target)

            if largest == 1:
                return True
            
            rest_sum = total - largest
            if rest_sum == 0:
                return False
            
            prev = largest % rest_sum
            
            if prev == 0:
                prev = rest_sum
            if prev < 1:
                return False
            
            total = rest_sum + prev

            if prev == largest:
                return False

            heapq.heappush_max(target, prev)


            


dummy_arr = [8,5]
solution = Solution()
print(solution.isPossible(dummy_arr))