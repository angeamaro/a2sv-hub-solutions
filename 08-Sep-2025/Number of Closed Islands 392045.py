# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = 1
            close = True

            while queue:
                i, j = queue.popleft()
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    close = False

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0:
                        grid[ni][nj] = 1
                        queue.append((ni, nj))

            return close

        res = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    if bfs(r, c):
                        res += 1
        return res