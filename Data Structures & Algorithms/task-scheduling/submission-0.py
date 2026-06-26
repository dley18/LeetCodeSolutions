class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_table = {}
        max_heap = []
        queue = []
        front = 0
        cycles = 0

        for task in tasks:
            if task in frequency_table:
                frequency_table[task] += 1
            else:
                frequency_table[task] = 1

        for (key, value) in frequency_table.items():
            heapq.heappush_max(max_heap, (value, key))

        while max_heap or front < len(queue):
            cycles += 1

            if max_heap:
                (freq, task) = heapq.heappop_max(max_heap)
                freq -= 1
                if freq > 0:
                    queue.append([cycles + n, freq, task])
                
            else:
                cycles = queue[front][0]
            
            if front < len(queue) and queue[front][0] <= cycles:
                freq = queue[front][1]
                task = queue[front][2]
                heapq.heappush_max(max_heap, (freq, task))
                front += 1
        
        return cycles
                    