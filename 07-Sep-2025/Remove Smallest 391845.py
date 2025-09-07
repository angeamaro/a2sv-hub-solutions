# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input())

def possible(arr):
    for i in range(1, n):
        if arr[i] - arr[i - 1] > 1:
            return False
    return True

for _ in range(t):
    n =  int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    if possible(arr):
        print("YES")
    else:
        print("NO")