# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
            n = len(nums)
            count = 0

            for i in range(n):
                aux = 0
                for j in range(i, n):
                    aux = gcd(aux, nums[j])
                    if aux < k:
                        break
                    if aux == k:
                        count += 1
            return count
            