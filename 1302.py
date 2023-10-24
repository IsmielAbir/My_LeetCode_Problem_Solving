# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ms = 0
        s = 0

        def dfs(node, level):
            nonlocal ms, s
            if not node:
                return 0
            
            if ms<level:
                ms = level
                s = 0
            if ms == level:
                s+=node.val
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)

        return s

        