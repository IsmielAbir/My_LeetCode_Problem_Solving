# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def add(root):
            if not root:
                return TreeNode(val)
            if val < root.val:
                root.left = add(root.left)
            else:
                root.right = add(root.right)
            return root
        
        return add(root)