# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x, y, dist in roads:
            graph[x].append((y, dist))
            graph[y].append((x, dist))

        q = deque([1])
        visited = set()
        visited.add(1)

        mini = float("inf")

        while q:
            curr = q.popleft()
            for nxt, dist in graph[curr]:
                mini = min(mini, dist)
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)
        return mini
        