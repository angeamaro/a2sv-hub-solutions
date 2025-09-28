# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        size = 2 * k + 1
        
        if size > n:
            return res
        
        window_sum = sum(nums[:size])
        res[k] = window_sum // size
        
        for i in range(size, n):
            window_sum += nums[i] - nums[i - size]
            res[i - k] = window_sum // size
        
        return res