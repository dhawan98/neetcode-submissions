class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxarea=0

        def dfs(r, c):
            if (r<0 or r>rows-1 or c<0 or c>cols-1 or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            area = 1
            area+=dfs(r, c+1)
            area+=dfs(r, c-1)
            area+=dfs(r-1, c)
            area+=dfs(r+1, c)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area = dfs(r, c)
                    maxarea= max(area, maxarea)
        return maxarea