# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def inOrder(root):
            if root:
                li.append(root.val)
                inOrder(root.left)
                inOrder(root.right)
        inOrder(root)
        f = Counter(li)
        maxx = max(f.values())
        return [i for i in f if f[i]==maxx]
        
        