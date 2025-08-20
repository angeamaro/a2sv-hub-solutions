# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            n ^= num
        return n