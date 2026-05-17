class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_data = sorted(enumerate(position), key=lambda x: x[1], reverse=True)
        sorted_indexes = [idx for idx, val in sorted_data]
        stack = []
        for idx in sorted_indexes:
            time = (target - position[idx]) / speed[idx]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)