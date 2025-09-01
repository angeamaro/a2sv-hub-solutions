# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        ans = 0
        visited = set()
        for stn in stones:
            counter = 0
            if (stn[0], stn[1]) in visited:
                continue
            bfs = deque()
            bfs.append(stn)
            visited.add((stn[0], stn[1]))
            while bfs:
                node = bfs.popleft()
                counter += 1
                for nxt in stones:
                        if (nxt[0], nxt[1]) not in visited and (nxt[0] == node[0] or nxt[1] == node[1]):
                            bfs.append(nxt)
                            visited.add((nxt[0], nxt[1]))
            ans += (counter - 1)
        return ans