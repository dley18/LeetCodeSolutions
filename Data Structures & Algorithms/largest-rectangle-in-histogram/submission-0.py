class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        ans = 0

        # 7,1,7,2,2,4
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:

                bar = stack.pop()
                current = i

                if stack:
                    left = stack[-1]
                else:
                    left = -1

                width = current - left - 1
                area = width * heights[bar]
                ans = max(ans, area)

            stack.append(i)

        while stack:

            bar = stack.pop()
            current = len(heights)

            if stack:
                left = stack[-1]
            else:
                left = -1

            width = current - left - 1
            area = width * heights[bar]
            ans = max(ans, area)

        return ans

sol = Solution()