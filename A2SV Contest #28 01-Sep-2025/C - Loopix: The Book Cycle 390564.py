# Problem: C - Loopix: The Book Cycle - https://codeforces.com/gym/632067/problem/C

t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of kids
    p = list(map(int, input().split()))  # Permutation
    
    res = [0] * n   # Result: cycle length for each kid
    
    for i in range(n):
        if res[i] == 0:   # Not yet calculated
            cycle = []
            cur = i
            
            # Traverse the cycle starting from i
            while cur not in cycle:
                cycle.append(cur)
                cur = p[cur] - 1  # Move to next (adjust for 0-based)
            
            size = len(cycle)  # Cycle length
            for idx in cycle:
                res[idx] = size
    
    print(*res)
