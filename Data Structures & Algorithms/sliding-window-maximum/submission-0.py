import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_arr = []

        l = 0

        for r in range(k, len(nums) + 1):
            window = nums[l:r]
            heapq.heapify_max(window)
            max_arr.append(heapq.heappop_max(window))
            l += 1

        return max_arr