# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        a = root.val
        b = root.left.val 
        c = root.right.val
        if a==(b+c):
            return True
        else:
            return False
        