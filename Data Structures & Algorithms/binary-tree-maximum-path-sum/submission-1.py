# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = -float('inf')

        def dfs(curr):
            if not curr:
                return 0
            l = max(dfs(curr.left), 0)
            r = max(dfs(curr.right), 0)
            
            path = curr.val + l + r
            self.best = max(self.best, path)
            return curr.val + max(l, r)
        
        dfs(root)
        return self.best
            
