# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        columns = [False] * n
        diagonal1 = [False] * (2 * n - 1)
        diagonal2 = [False] * (2 * n - 1)

        def back(i):
            nonlocal count
            if i == n:
                count += 1
                return
            for j in range(n):
                if columns[j] or diagonal1[j + i] or diagonal2[j - i + n - 1]:
                    continue
                columns[j] = diagonal1[j + i] = diagonal2[j - i + n - 1] = True
                back(i + 1)
                columns[j] = diagonal1[j + i] = diagonal2[j - i + n - 1] = False

        back(0)
        return count