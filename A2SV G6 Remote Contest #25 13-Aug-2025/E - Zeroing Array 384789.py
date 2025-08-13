# Problem: E - Zeroing Array - https://codeforces.com/gym/628023/problem/E

n = int(input())

arr = list(map(int,input().split()))

total = maximum = 0

for num in arr:
    total += num
    maximum = max(maximum, num)

if total % 2 == 1 or maximum > total - maximum:
    print('NO')
else:
    print('YES')