# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))  
        res = []

        for s, e in intervals:
            idx = bisect_left(starts, (e,))
            if idx < n:
                res.append(starts[idx][1])
            else:
                res.append(-1)
        
        return res
        
        