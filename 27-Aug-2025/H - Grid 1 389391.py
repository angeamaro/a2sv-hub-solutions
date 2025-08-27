# Problem: H - Grid 1 - https://atcoder.jp/contests/dp/tasks/dp_h

MOD = 10**9 + 7

h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
  
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
    
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            dp[i][j] = 0
            continue
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
        dp[i][j] %= MOD
    
print(dp[h-1][w-1])
