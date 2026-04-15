class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        n = len(words)
        left_index = (startIndex - 1 + n) % n
        right_index = (startIndex + 1) % n

        steps = 1

        while right_index != startIndex or left_index != startIndex:
            if words[right_index] == target or words[left_index] == target:
                return steps
            
            steps += 1
            right_index = (right_index + 1) %n
            left_index = (left_index - 1 + n) % n
        
        return -1