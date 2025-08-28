# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def dfs(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
                
            path.append("L")
            if dfs(node.left, target, path ):
                return True

            path.pop()

            path.append("R")
            if dfs(node.right,target,path):
                return True
            
            path.pop()
            return False
        
        start = []
        dfs(root,startValue,start)
        dest = []
        dfs(root,destValue,dest)

        i = 0
        n,m = len(start), len(dest)

        while i < n and i < m and start[i] == dest[i]:
            i += 1

        up = "U" * (n - i)    
        down = "".join(dest[i:])  
        return up + down 

         
                
        