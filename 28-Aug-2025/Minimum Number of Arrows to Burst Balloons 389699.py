# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 0

        pos = points[0][1]

        for start,end in points:
            if start > pos:
                count += 1
                pos = end
        return count + 1
        