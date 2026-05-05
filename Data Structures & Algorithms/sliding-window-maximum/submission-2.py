class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        max_arr = []

        for r in range(len(nums)):            
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)
            
            if window[0] < r - k + 1:
                window.popleft()

            if r >= k - 1:
                max_arr.append(nums[window[0]])

        return max_arr

            
            
