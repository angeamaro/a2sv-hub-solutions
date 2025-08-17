# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        memo = {}
        
        blocked = False
        for i in range(1, m + 1):
            if obstacleGrid[i-1][0] == 1:
                blocked = True
            memo[(i, 1)] = 0 if blocked else 1
        
        blocked = False
        for j in range(1, n + 1):
            if obstacleGrid[0][j-1] == 1:
                blocked = True
            memo[(1, j)] = 0 if blocked else 1
        
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                if obstacleGrid[i-1][j-1] == 1:
                    memo[(i, j)] = 0
                else:
                    memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]
        
        return memo[(m, n)]

        