# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])  
        res = []  

        # Loop through all possible diagonals
        for i in range(m + n - 1):
            aux = [] 

            # Starting point of the diagonal
            row = 0 if i < n else i - n + 1
            col = i if i < n else n - 1

            # Collect all elements in this diagonal
            while row < m and col >= 0:
                aux.append(mat[row][col])
                row += 1
                col -= 1
            
            # Reverse every other diagonal
            if i % 2 == 0:
                aux.reverse()
            
            res.extend(aux)
        return res
