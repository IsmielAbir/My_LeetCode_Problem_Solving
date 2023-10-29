"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        li = []
        def post(root):
            if root:
                for i in root.children:
                    post(i)
                li.append(root.val)
            return li
        return post(root)