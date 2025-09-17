# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            curr = nums[i]
            for j in range(i,n):
                curr = lcm(curr, nums[j])
                if curr == k:
                    res += 1
                if curr > k or k % curr != 0:
                    break
        return res
        