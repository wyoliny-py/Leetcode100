# 235. Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Recursive
        # lca = [root]
        # def search(root):
        #     if not root:
        #         return
            
        #     lca[0] = root
        #     if root is p or root is q:
        #         return
        #     elif root.val < p.val and root.val < q.val:
        #         search(root.right)
        #     elif root.val > p.val and root.val > q.val:
        #         search(root.left)
        #     else:
        #         return
        # search(root)
        # return lca[0]
    
        # Iterative
        while root:
            if min(p.val, q.val) > root.val:
                root = root.right
            elif max(p.val, q.val) < root.val:
                root = root.left
            else:
                return root  
        
        # O(n)