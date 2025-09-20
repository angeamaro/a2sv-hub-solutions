# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, cl = len(matrix), len(matrix[0])
        left, right = 0, rl * cl - 1   

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, cl)
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False