# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        arr = [True] * n
        arr[0] = arr[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if arr[i]:
                for j in range(i * i, n , i):
                    arr[j] = False
        ans = 0
        for i in range(n):
            if arr[i]:
                ans += 1
        return ans
                             

        