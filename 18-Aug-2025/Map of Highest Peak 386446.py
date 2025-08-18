# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n,m = len(isWater), len(isWater[0])
        queue = deque()
        visited = set()
        res = [ [-1] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if isWater[r][c]:
                    queue.append((r,c))
                    visited.add((r,c))
                    res[r][c] = 0

        while queue:
            r, c = queue.popleft()
            h = res[r][c]

            neighbors = [(r + 1 , c), (r, c + 1), (r - 1 , c), (r, c - 1)]

            for nr,nc in neighbors:
                if ( nr < 0 or nc < 0 or nr == n or nc == m or (nr,nc) in visited):
                    continue
                queue.append((nr,nc))
                visited.add((nr,nc))
                res[nr][nc] = h + 1

        return res