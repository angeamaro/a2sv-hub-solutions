# Problem: B - Kinda Swap, Kinda Rock - https://codeforces.com/gym/628023/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    for i in range(min(k, n)):
        if b[i] > a[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break

    print(sum(a))
