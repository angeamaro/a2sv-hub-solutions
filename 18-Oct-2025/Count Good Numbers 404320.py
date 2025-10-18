# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        even = (n + 1) // 2
        odd = n // 2
        
        return (pow(5, even, MOD) * pow(4, odd, MOD)) % MOD
        