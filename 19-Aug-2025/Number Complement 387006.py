# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        length = num.bit_length()
        return num ^ ((1 << length) - 1)
        