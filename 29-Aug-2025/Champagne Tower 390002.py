# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = poured
        
        for r in range(query_row):
            for c in range(len(dp[r])):
                if dp[r][c] > 1:
                    excess = dp[r][c] - 1
                    dp[r][c] = 1
                    dp[r + 1][c] += excess / 2.0
                    dp[r + 1][c + 1] += excess/ 2.0

        return min(1, dp[query_row][query_glass])
        