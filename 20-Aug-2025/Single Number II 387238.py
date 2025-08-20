# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0  

        for num in nums:
            # add current num to ones, remove if is already in twos
            ones = (ones ^ num) & ~twos
            # add current num to twos, remove if is already in ones
            twos = (twos ^ num) & ~ones

        return ones
        