# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
arr = list(map(int, input().split()))

l, r = 0, n - 1
sereja = dima = 0
turn = 0  

while l <= r:
    if arr[l] > arr[r]:
        x = arr[l]
        l += 1
    else:
        x = arr[r]
        r -= 1

    if turn == 0:
        sereja += x
    else:
        dima += x

    turn ^= 1  

print(sereja, dima)
