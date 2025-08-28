# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0

        comp = intervals[0][1]
        for i in range (1, len(intervals)):
            if comp > intervals[i][0]:
                count += 1
            else:
                comp = intervals[i][1]
        return count 
        