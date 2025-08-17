# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = defaultdict(int)
    
    for i in range(n):
        key = arr[i] - i
        freq[key] += 1

    total = 0
    for count in freq.values():
        if count >= 2:
            total += count * (count - 1) // 2
    
    print(total)
