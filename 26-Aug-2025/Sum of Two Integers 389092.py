# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
            mask = 0xFFFFFFFF      
            longest = 0x7FFFFFFF   

            while b != 0:
                s = (a ^ b) & mask
                carry = ((a & b) << 1) & mask
                a, b = s, carry

            return a if a <= longest else ~(a ^ mask)

        