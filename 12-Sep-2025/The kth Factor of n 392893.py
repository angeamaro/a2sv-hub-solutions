# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 1
        for i in range(1,n + 1):
            if n % i == 0 and count == k:
                return i
            elif n % i == 0:
                count += 1
        return -1


        
        