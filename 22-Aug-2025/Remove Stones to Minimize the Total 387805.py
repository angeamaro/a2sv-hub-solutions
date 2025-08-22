# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)

        for i in range(k):
            largest = -heapq.heappop(heap)   
            reduced = largest - largest // 2     
            heapq.heappush(heap, -reduced)   

        return -sum(heap)
        