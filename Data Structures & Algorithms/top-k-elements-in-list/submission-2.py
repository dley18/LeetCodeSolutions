class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums) + 1)]
        count_table = {}
        top_k = []

        for num in nums:
                count_table[num] = 1 + count_table.get(num, 0)
        for num, count in count_table.items():
            buckets[count].append(num)
        
        for bucket in reversed(buckets):
            for num in bucket:
                if k > 0:
                    top_k.append(num)
                    k -= 1

        return top_k