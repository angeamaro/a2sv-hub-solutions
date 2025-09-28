# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n  = int(input())

nums = list(map(int,input().split()))

# Checks if there's at leats one even and odd number in the array
has_even = any(num % 2 == 0 for num in nums)
has_odd = any(num % 2 == 1 for num in nums)

# If there is at least one even and one odd number,
# it's possible to swap the array to sort him lexicographically
if has_even and has_odd:
    nums.sort()

print(*nums)
    