# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        cords = [x for x, _ in points]
       
        cords.sort()
        
        maximum = 0
        for i in range(1, len(cords)):
            maximum = max(maximum, cords[i] - cords[i - 1])
        return maximum
        