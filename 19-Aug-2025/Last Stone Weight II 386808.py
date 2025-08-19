# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_stones = sum(stones)
        mid = ceil(sum_stones / 2)

        memo = {}

        def back(i, tot):
            if tot >= mid or i == len(stones):
                return abs(tot - (sum_stones - tot))
            if (i,tot) in memo:
                return memo[(i,tot)]
            memo[(i,tot)] = min(back(i + 1, tot), back(i + 1, tot + stones[i]))
            return memo[(i,tot)]
        return back(0,0)