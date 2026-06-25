import random
class Solution:
    def partition(self, arr, l, r) -> int:
        pivot_idx = random.randint(l, r)
        arr[pivot_idx], arr[r] = arr[r], arr[pivot_idx]
        pivot = arr[r]
        i = l

        for j in range(l, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        arr[i], arr[r] = arr[r], arr[i]
        return i

    def recurse(self, arr, l, r, k) -> int:
        if l == r:
            return arr[l]

        idx = self.partition(arr, l, r)

        if idx == self.target:
            return arr[idx]

        if idx > self.target:
            return self.recurse(arr, l, idx - 1, k)
        else:
            return self.recurse(arr, idx + 1, r, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.target = len(nums) - k
        res = self.recurse(nums, 0, len(nums) - 1, k)
        return res
        

        