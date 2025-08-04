# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in rows[r] 
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3,c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3,c // 3)].add(board[r][c])
        return True
                    


        