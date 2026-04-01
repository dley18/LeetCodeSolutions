from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        queue = deque((tickets[i], i == k) for i in range(len(tickets)))
        time = 0

        while queue:

            count, is_k = queue.popleft()

            count -= 1
            time += 1

            if count == 0:
                if is_k:
                    return time
            else:
                queue.append((count, is_k))



