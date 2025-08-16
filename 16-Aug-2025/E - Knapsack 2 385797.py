# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

INF = 10**15

N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

max_val = sum(v for _, v in items)

dp = [INF] * (max_val + 1)
dp[0] = 0

for w, v in items:
    for val in range(max_val, v - 1, -1):
        dp[val] = min(dp[val], dp[val - v] + w)

ans = max(val for val in range(max_val + 1) if dp[val] <= W)
print(ans)