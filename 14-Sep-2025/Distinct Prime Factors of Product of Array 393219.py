# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes =  set()

        for num in nums:
            div = 2
            while num != 1:
                if num % div == 0:
                    primes.add(div)
                    num //= div
                else:
                    div += 1
        
        return len(primes)


