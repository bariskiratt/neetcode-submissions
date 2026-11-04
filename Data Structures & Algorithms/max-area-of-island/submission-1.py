class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0
        def bfs(r,c):
            maxArea = 0
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            while q:
                row, col = q.popleft()
                maxArea += 1
                for dr,dc in directions:
                    nr,nc = dr + row , dc + col
                    if(nr <0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
            return maxArea
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(bfs(r,c),res)
        return res

