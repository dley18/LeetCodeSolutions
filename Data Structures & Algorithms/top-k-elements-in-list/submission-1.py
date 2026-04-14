class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums))]
        count_table = {}
        top_k = []

        for num in nums:
            if num in count_table:
                count_table[num] += 1
                buckets[count_table[num] - 2].remove(num)
            else:
                count_table[num] = 1

            buckets[count_table[num] - 1].append(num)
        
        for bucket in reversed(buckets):
            for num in bucket:
                if k > 0:
                    top_k.append(num)
                    k -= 1

        return top_k