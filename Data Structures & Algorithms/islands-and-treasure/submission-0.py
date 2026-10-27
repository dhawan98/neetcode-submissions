class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        inf = 2147483647
        q = deque()

        # visit [[False] for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        def bfs (r, c, dist):
            if (r< 0 or r>rows-1 or c<0 or c>cols-1 or grid[r][c]!=inf):
                return 
            grid[r][c] = dist
            q.append((r, c))
        while q:
            r, c = q.popleft()
            dist = grid[r][c] + 1
            bfs(r + 1, c, dist)                  # Down
            bfs(r - 1, c, dist)                  # Up
            bfs(r, c + 1, dist)                  # Right
            bfs(r, c - 1, dist)                  # Left