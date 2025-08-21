# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        xor = n ^ (n >> 1)
        return (xor & (xor + 1)) == 0

        