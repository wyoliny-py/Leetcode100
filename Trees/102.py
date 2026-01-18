# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        q = deque([root])
        answer = []
        while q:
            level = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            answer.append(level)
        return answer
