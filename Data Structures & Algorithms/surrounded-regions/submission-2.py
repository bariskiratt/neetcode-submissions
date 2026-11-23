class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        unsurrounded = set()
        for r in range(ROWS):
            for c in range(COLS):
                if((r ==0 or c == 0 or r == ROWS-1 or c == COLS-1) and board[r][c] == "O"):
                    q.append([r,c])
                    unsurrounded.add((r,c))

        
        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                nr,nc = row + dr , col + dc
                if(nr < 0 or nc < 0 or nr == ROWS or nc == COLS or board[nr][nc] == "X" or (nr,nc) in unsurrounded):
                    continue
                q.append((nr,nc))
                unsurrounded.add((nr,nc))

        
            

        for r in range(ROWS):
                for c in range(COLS):
                    if (r,c) not in unsurrounded and board[r][c] == 'O':
                        board[r][c] = 'X'