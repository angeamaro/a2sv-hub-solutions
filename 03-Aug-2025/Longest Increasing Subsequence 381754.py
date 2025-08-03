# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [0] * len(nums)
        
        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] == 0:
                memo[i] = 1
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        memo[i] = max(memo[i], 1 + dp(j))
            return memo[i]
        
        max_len = 0
        for i in range(len(nums)):
            max_len = max(max_len, dp(i))
        
        return max_len

        