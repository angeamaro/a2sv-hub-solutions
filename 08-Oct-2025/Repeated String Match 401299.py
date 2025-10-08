# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        rep = len(b) // len(a) + 2 
        for i in range(rep + 1):
            if b in a * i:
                return i
        return -1