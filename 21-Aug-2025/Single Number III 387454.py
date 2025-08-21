# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor =  0
        for num in nums:
            xor ^=  num

        diff = 1
        while not(diff & xor):
            diff <<= 1

        a = b = 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        return [a,b]

