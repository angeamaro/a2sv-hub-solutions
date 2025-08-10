# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = []

        for row in range(min(k, n)):  
            heapq.heappush(min_heap, (matrix[row][0], row, 0))

        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))
        
        return val
            