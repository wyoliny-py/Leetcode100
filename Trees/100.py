# 100. Same Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def is_node(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False

            if p.val != q.val:
                return False

            return is_node(p.left, q.left) and is_node(p.right, q.right)
        return is_node(p, q)