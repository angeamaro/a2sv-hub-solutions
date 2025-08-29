# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n,m = len(maze), len(maze[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        er, ec = entrance
        q = deque([(er,ec,0)])
        
        def inbounds(r, c):
            if r < n and c < m and r >= 0 and c >= 0 and maze[r][c] != "+":
                return True
            return False
        
        def is_exit(r,c):
            if r == 0 or c == 0 or r == n - 1 or c == m - 1:
                return True
            return False 

        maze[er][ec] = "+"

        while q:
            row,col,dist = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if inbounds(nr,nc):
                    if is_exit(nr,nc):
                        return dist + 1
                    maze[nr][nc] = "+"
                    q.append((nr,nc, dist + 1))
        return -1


                 
        