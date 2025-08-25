# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1 << n): 
            res.append(i ^ (i >> 1))
        return res
        