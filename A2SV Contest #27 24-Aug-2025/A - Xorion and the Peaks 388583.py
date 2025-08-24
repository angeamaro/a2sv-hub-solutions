# Problem: A - Xorion and the Peaks - https://codeforces.com/gym/630556/problem/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k > (n - 1) // 2:
        print(-1)
        continue
    
    a = list(range(1, n+1))    
    for i in range(1, k+1):
        a[2*i-1], a[2*i] = a[2*i], a[2*i-1]
        
    print(" ".join(map(str, a)))