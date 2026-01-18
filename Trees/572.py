# 572. Subtree of Another Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def sameTree(p, q):
            if (not p and not q):
                return True
            elif (not p and q) or (not q and p):
                return False
            
            if p.val != q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def sameSubTree(root):
            if not root:
                return False
            
            if sameTree(root, subRoot):
                return True
            
            return sameSubTree(root.left) or sameSubTree(root.right)
        
        return sameSubTree(root)
    
    # O(n * m)