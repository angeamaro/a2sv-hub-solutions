# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            
            for nei, w in graph[start]:
                if nei in visited:
                    continue
                res = dfs(nei, end, visited)
                if res != -1.0:
                    return w * res
            return -1.0
        
        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))
        
        return res

        