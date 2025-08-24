# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import defaultdict 
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        reds = defaultdict(list)
        blues = defaultdict(list)

        for u, v in redEdges:
            reds[u].append(v)
        for u, v in blueEdges:
            blues[u].append(v)

        res = [-1] * n

        q = deque()
        q.append((0, -1)) 
        visited = set([(0, -1)])

        dist = 0
        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                if res[node] == -1:
                    res[node] = dist

                if color != 0:  
                    for nei in reds[node]:
                        if (nei, 0) not in visited:
                            visited.add((nei, 0))
                            q.append((nei, 0))
                if color != 1:  
                    for nei in blues[node]:
                        if (nei, 1) not in visited:
                            visited.add((nei, 1))
                            q.append((nei, 1))
            dist += 1

        return res
