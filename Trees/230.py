# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ''' Pre Order DFS '''


        # stk = [root]
        # listik = []

        # while stk:
        #     node = stk.pop()
        #     listik.append(node.val)
        #     if node.right: stk.append(node.right)
        #     if node.left: stk.append(node.left)
        
        # return sorted(listik)[k-1]
        # O(n log n)

        ''' In order DFS '''


        # answer = []

        # def in_order(node):
        #     if not node:
        #         return
        #     in_order(node.left)
        #     answer.append(node.val)
        #     in_order(node.right)

        # in_order(root)
        # return answer[k-1]
        # O(n)



        ''' In order DFS with no array '''

        count = [k]
        ans = [0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if count[0] == 1:
                ans[0] = node.val
            
            count[0] = count[0] - 1

            if count[0] > 0:
                dfs(node.right)
        
        dfs(root)
        return ans[0]
    
        # O(n)