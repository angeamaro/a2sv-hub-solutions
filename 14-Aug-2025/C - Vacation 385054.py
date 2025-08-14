# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
a = []
b = []
c = []

for _ in range(n):
    x, y, z = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)

prevA, prevB, prevC = 0, 0, 0

for i in range(n):
    curA = max(prevB, prevC) + a[i]
    curB = max(prevA, prevC) + b[i]
    curC = max(prevA, prevB) + c[i]
    prevA, prevB, prevC = curA, curB, curC

print(max(prevA, prevB, prevC))
