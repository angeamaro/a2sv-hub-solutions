# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(1, n):
            for j in range(n):
                prev = matrix[i-1][j]
                if j > 0:
                    prev = min(prev, matrix[i-1][j-1])
                if j < n-1:
                    prev = min(prev, matrix[i-1][j+1])
                matrix[i][j] += prev
        
        return min(matrix[n-1])
        