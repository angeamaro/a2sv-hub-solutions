# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)

        for a,b in pairs:
            union(a,b)
        
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)
        
        res = list(s)

        for index in groups.values():
            c = sorted(res[i] for i in index) 
            for i, ch in zip(sorted(index), c):
                res[i] = ch
        
        return "".join(res)


        