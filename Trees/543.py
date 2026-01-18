# 543. Diameter of Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_diameter = [0]
        def height(root):
            if not root:
                return 0
            
            height_left = height(root.left)
            height_right = height(root.right)

            max_diameter[0] = max(max_diameter[0], height_left + height_right)

            return 1 + max(height_left, height_right)
        height(root)
        return max_diameter[0]