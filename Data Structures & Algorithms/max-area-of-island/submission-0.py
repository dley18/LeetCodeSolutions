class Solution:

    def isValidSpot(self, x, y):
        if x >= len(self.grid[0]) or x < 0:
            return False

        if y >= len(self.grid) or y < 0:
            return False

        if self.grid[y][x] == 0:
            return False

        return True

    def dfs(self, x, y):

        if not self.isValidSpot(x, y):
            return

        self.grid[y][x] = 0
        self.area += 1

        self.dfs(x + 1, y)
        self.dfs(x - 1, y)
        self.dfs(x, y + 1)
        self.dfs(x, y - 1)

        return

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.grid = grid
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if self.grid[i][j] == 1:
                    self.area = 0
                    self.dfs(j, i) 
                    result = max(result, self.area)

        return result