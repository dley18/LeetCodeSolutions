class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(nums)
        self.max_length = k
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.max_length:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        
