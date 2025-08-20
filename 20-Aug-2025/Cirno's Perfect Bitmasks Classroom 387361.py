# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

n = int(input())
 
for _ in range(n):
    num = int(input())
    if num == 1:
        print(3)
    elif num & (num - 1) == 0:
        print(num + 1)
    else:
        print(num & -num)