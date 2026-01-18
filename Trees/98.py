# 98. Validate Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(node, smaller, biggest):
            if not node:
                return True
            
            if node.val <= smaller or node.val >= biggest:
                return False
            
            return is_valid(node.left, smaller, node.val) and is_valid(node.right, node.val, biggest)
        return is_valid(root, float('-inf'), float('inf'))
        # O(n)