class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0

        start = 0
        end = len(heights) - 1
        while start < end:
            water = (end - start) * min(heights[start], heights[end])
            res = max(res, water)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return res