# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
                5
        2               8
    6       1       2
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        root_val = root.val
        def dfs(curr, max_val):
            res = 0
            if curr.left:
                res += dfs(curr.left, max(max_val, curr.val))

            if curr.right:
                res += dfs(curr.right, max(max_val, curr.val))
            
            
            if curr.val >= max_val:
                res += 1
            
            return res
        return dfs(root, root.val)





