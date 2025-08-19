# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def prof(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in memo:
                return memo[(i, can_buy)]

            cool = prof(i + 1, can_buy)

            if can_buy:
                buy = prof(i + 1, False) - prices[i]
                memo[(i, can_buy)] = max(buy, cool)

            else:
                sell = prof(i + 2, True) + prices[i]
                memo[(i, can_buy)] = max(sell, cool)

            return memo[(i, can_buy)]

        return prof(0, True)