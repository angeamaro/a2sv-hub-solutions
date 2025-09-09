# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int: 
        n = len(nums)
        if n < 2:
            return 0
        
        nums.sort()
        maxi = 0
        for i in range(1, n):
            maxi = max(maxi, nums[i] - nums[i - 1])
        return maxi

        