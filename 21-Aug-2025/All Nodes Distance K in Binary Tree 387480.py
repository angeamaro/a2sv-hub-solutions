# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        
        graph =  defaultdict(list)
        q = deque([root])

        while q:
            node = q.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)

        res =  []
        visited = set([target])
        q = deque([(target, 0)])

        while q :
            node, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        q.append((edge, dist + 1))
        return res
        