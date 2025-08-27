# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for bit in range(31, -1, -1): 
            mask |= (1 << bit)
            pref = {num & mask for num in nums}
            candidate = max_xor | (1 << bit)
            if any((candidate ^ p) in pref for p in pref):
                max_xor = candidate
        return max_xor

        