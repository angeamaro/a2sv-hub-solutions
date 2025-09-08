# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            pos = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1

        res = 0
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1
