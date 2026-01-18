# 110. Balanced Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        # 1  O ( n  )
        # def dfs(node):
        #     if not node:
        #         return True, 0
        #     left_balanced, left_height = dfs(node.left)
        #     right_balanced, right_height = dfs(node.right)
        #     balanced = (left_balanced and right_balanced and 
        #                abs(left_height - right_height) <= 1)
        #     height = 1 + max(left_height, right_height)
            
        #     return balanced, height
        # balanced, _ = dfs(root)
        # return balanced


        # 2 (  O(n)  )
        balanced = [True]
        def height(root):
            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return balanced[0]
