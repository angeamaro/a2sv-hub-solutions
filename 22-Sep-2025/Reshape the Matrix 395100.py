# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n,m = len(mat),len(mat[0])

        if n * m != r * c:
            return mat

        aux = []
        for i in range(n):
            for j in range(m):
                aux.append(mat[i][j])

        res = []

        for i in range(r):
            res.append(aux[i * c :(i + 1) * c])
        
        return res

        